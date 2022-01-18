import pandas as pd
import numpy as np
from helper_functions import Solution
DAY = 5

# overlapping lines
class Day5():

    def get_data(self):
        df = pd.read_csv("data\\day5.txt", header=None)
        df_split = pd.concat([df.loc[:,0], pd.DataFrame(list(df.loc[:,1].str.split(' '))), df.loc[:,2]], axis=1, ignore_index=True)

        return df_split.drop(columns=[2]).rename(columns={0:'x1', 1:'y1',3:'x2',4:'y2'}).astype('int16')

    # straight lines are horizontal or vertical, but not diagonal
    def remove_diagonals(self, data):
        straight_lines = (data.loc[:,'x1'] == data.loc[:,'x2']) | (data.loc[:,'y1'] == data.loc[:,'y2'])
        return data.loc[straight_lines, :]


    def fill_board(self, data):
        for row in data:
            if row[0] <= row[2]:
                r_idx = np.arange(row[0]-1, row[2])
            else:
                r_idx = np.flip(np.arange(row[2]-1,row[0]))

            if row[1] <= row[3]:
                c_idx = np.arange(row[1]-1, row[3])
            else:
                c_idx = np.flip(np.arange(row[3]-1,row[1]))
            day5.board[r_idx, c_idx] += 1


    def solve(self, is_part_a):
        data = day5.get_data()
        if is_part_a:
            print("Removing diagonals")
            hv_lines = np.array(day5.remove_diagonals(data).values)
        else:
            hv_lines = np.array(data.values)

        self.x_size = data.loc[:,['x1','x2']].max().max()
        self.y_size = data.loc[:,['y1','y2']].max().max()
        self.board = np.zeros([self.x_size, self.y_size])

        day5.fill_board(hv_lines)

        result = np.where(self.board >= 2,1, 0).sum()
        # result = None
        return result



day5 = Day5()
solution_a = day5.solve(True)

solution_b = day5.solve(False)



# third party solution after the fact to learn better techniques
#Soln courtesy of hyper-neutrino -> https://github.com/hyper-neutrino/advent-of-code/blob/main/2021/day5p2.py
grid = {}
with open("data\\day5.txt", mode='r') as f:
    data = f.read()
    data = data.splitlines()

for line in data[0:10]:
    l, r = line.split(" -> ")
    x1, y1 = map(int, l.split(","))
    x2, y2 = map(int, r.split(","))
    dx = x2 - x1
    dy = y2 - y1
    if dx: dx = dx // abs(dx)
    if dy: dy = dy // abs(dy)
    print(dx,dy)
    x = x1
    y = y1

    while True:
        grid[(x, y)] = grid.get((x, y), 0) + 1
        if x == x2 and y == y2:
            break
        x += dx
        y += dy