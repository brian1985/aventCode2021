import numpy as np
import re
from time import perf_counter as pfc

DAY = 13


#  Oragami
class Day13():

    def __init__(self):
        self.data = None

    def get_data(self):
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            self.data = f.readlines()
            self.markers = []
            self.folds = []
            self.x_max = 0
            self.y_max = 0
            for line in self.data:
                if 'fold' in line:
                    if 'x=' in line:
                        self.folds.append(('x',int(line.strip().split("=")[1])))
                    else:
                        self.folds.append(('y', int(line.strip().split("=")[1])))
                elif line.strip():
                    point = [int(val.strip()) for val in line.strip().split(',')]
                    self.markers.append( point )
                    if point[0] > self.x_max:
                        self.x_max = point[0]
                    if point[1] > self.y_max:
                        self.y_max = point[1]
                else:
                    print("Empty line", line)

    def fill_board(self):
        day13.board = np.zeros(shape=(day13.y_max+1, day13.x_max+1))
        for marker in day13.markers:
            day13.board[marker[1],marker[0]] = 1

    def fold_x(self, col):
        left_board = day13.board[:,:col]
        right_board = day13.board[:, col+1:]
        if right_board.shape != left_board.shape:
            print("dim mismatch for now. Need padding")
        flipped_board = np.fliplr(right_board)
        self.board = left_board + flipped_board


    def fold_y(self, row):
        top_board = day13.board[:row, :]
        bottom_board = np.zeros(top_board.shape)
        bottom_idx = day13.board[row+1:, :].shape[0]
        # print("shapes:",top_board.shape, bottom_board[:bottom_idx, :].shape,bottom_idx, day13.board[row+1:, :].shape)
        bottom_board[top_board.shape[0] - bottom_idx:, :] = np.flipud(day13.board[row+1:, :])
        day13.board = top_board + bottom_board

    def solve(self):
        day13.fill_board()

        # self.folds = [self.folds[0],]
        for idx, fold in enumerate(self.folds):
            #  answer to part a
            if idx == 1:
                num_nonzero = np.where(self.board != 0, 1, 0).sum().sum()

            if fold[0] == 'x':
                print("x", fold[1])
                self.fold_x(fold[1])
            else:
                print("y", fold[1])
                self.fold_y(fold[1])

        return num_nonzero , np.where(self.board >=1,1,0)

    def solve_b(self):
        pass



#1061
day13 =Day13()
day13.get_data()
start = pfc()
solution_a, solution_b = day13.solve()
print(pfc()-start)