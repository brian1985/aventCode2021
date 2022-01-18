import pandas as pd
import numpy as np
from helper_functions import Solution
DAY = 4


class DayFour(Solution):
    def __init__(self):
        super(DayFour, self).__init__()
        self._mask = None
        self._filled_spaces = None
        self.id = None
        self._winning_direction = None

    def get_data(self):
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            formatted_data = []
            bingo_balls = f.readline()
            bingo_boards = f.readlines()

        for i, line in enumerate(bingo_boards):
            bingo_boards[i] = bingo_boards[i].strip()

        formatted_data = [x.strip() for x in bingo_boards if x.strip()]
        formatted_data = [x.split() for x in formatted_data]
        formatted_data = np.array(formatted_data, dtype='int16')
        formatted_data_final = formatted_data.reshape([100,5,5])

        self._bingo_cards = formatted_data_final
        self._bingo_balls = [int(x) for x in bingo_balls.split(",")]
        return formatted_data_final


    def mask_cards(self, val_to_mask):
        mask = data == val_to_mask
        self._filled_spaces = self._filled_spaces - mask


    def play_until_first_winner(self):
        col_sums = np.sum(self._filled_spaces, axis=1)
        row_sums = np.sum(self._filled_spaces, axis=2)

        if np.min(row_sums) == 0:
            self._winning_direction = 'row'
            return False
        elif np.min(col_sums) == 0:
            self._winning_direction = 'col'
            return False
        else:
            return True, None

    def play_until_last_winner(self):
        col_sums = np.sum(self._filled_spaces, axis=1)
        row_sums = np.sum(self._filled_spaces, axis=2)

        zero_rows = np.nonzero(np.min(row_sums, axis=1) == 0)
        zero_cols = np.nonzero(np.min(col_sums, axis=1) == 0)

        # catch bug mentioned below? needs testing
        if len(set(zero_rows[0]).union(set(zero_cols[0]))) == self._bingo_cards.shape[0]:
            return False

        self._winning_boards = set(zero_rows[0]).union(set(zero_cols[0]))
        print(len(day4._winning_boards))
        # if more than 2 or more have not won, return True (continue), else False
        # todo: There is a potential bug if the last X cards all win at the same time. This would then
        # The last mask would then cover more than one. This would exit, but fail to find the last one.
        if len(self._winning_boards) < self._bingo_cards.shape[0]:
            return True
        else:
            return False

    def get_winning_card_id(self):
        if self._winning_direction == 'row':
            totals = self._filled_spaces.sum(axis=2)
            return np.nonzero(totals == 0)[0][0]
        if self._winning_direction == 'col':
            totals = self._filled_spaces.sum(axis=1)
            return np.nonzero(totals == 0)[0][0]

    def get_last_winning_card_id(self):
        winning_board = set(list(np.arange(0, 100))).difference(self._winning_boards)
        if len(winning_board) > 1:
            return "No Solution"
        else:
            return winning_board.pop()

    def get_winning_total(self):
        desired_card = self._bingo_cards[self.id, :, :]
        filled_spaces = self._filled_spaces[self.id, :, :]

        #  counter is one past the successful finish
        result = np.multiply(desired_card, filled_spaces) * self.last_pulled_ball

        result = result.sum()

        return result

    def solve(self, winning_position='first'):
        # winning position should be 'first' or 'last'
        self._mask = np.ndarray(self._bingo_cards.shape)
        self._filled_spaces = np.ones(self._bingo_cards.shape)
        self._winning_boards = set()

        counter = 0
        if winning_position == 'first':
            while self.play_until_first_winner():
                self.mask_cards(self._bingo_balls[counter])
                self.last_pulled_ball = self._bingo_balls[counter]
                counter += 1

            self.id = self.get_winning_card_id()

        elif winning_position == 'last':
            while self.play_until_last_winner():
                self.mask_cards(self._bingo_balls[counter])
                self.last_pulled_ball = self._bingo_balls[counter]
                counter += 1

            self.id = self.get_last_winning_card_id()


        else:
            return "invalid winning_position received. type a lowercase only of 'first' or 'last'"

        self.last_pulled_ball = self._bingo_balls[counter - 1]
        result = self.get_winning_total()

        return result


day4 = DayFour()
data = day4.get_data()
solution_a = day4.solve('first')
solution_b = day4.solve('last')

last_card = day4._bingo_cards[68,:,:]
filled = day4._filled_spaces[68,:,:]

(last_card * filled).sum()

# not 25160
# not 15729
