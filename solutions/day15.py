import numpy as np
from time import perf_counter as pfc
from queue import PriorityQueue

DAY = 15


#  Optimized pathing
#used a hint on this one (first time :( )
# got idea to do rolling sum across the entire row and column and then use recursion as dynamic programming
# my solution is solution(). hint_solution() is using hint
class Day15():

    def __init__(self):
        self.cave = None

    def get_data(self, is_test=True):
        if is_test:
            text = '_test'
        else:
            text = ""

        with open(f"data\\day{DAY}{text}.txt", mode='r') as f:
            lines = f.readlines()
            size = len(lines[0].strip())
            cave = [int(l) for line in lines for l in line.strip()]
            day15.cave = np.array(cave).reshape((-1,size))


    def sum_row_col(self, k):
        for i in range(k,day15.cave.shape[0]):
            # print(k,i,day15.cave.shape, list(range(k,day15.cave.shape[0]-1)))
            day15.cave[i, k] += np.min([day15.cave[i,k-1], day15.cave[i-1,k]])

        for j in range(k+1,day15.cave.shape[1]):
            # print(k,j,day15.cave.shape,list(range(k+1,day15.cave.shape[1]-1)))
            day15.cave[k, j] += np.min([day15.cave[k-1,j], day15.cave[k,j-1]])

    # turns out you can also go up and left, so need something called Dijkstra algorithm.
    # Algorithm steps
    # 1) build nodes (location on the grid)
    # 2) build edges (value at location) 1 connection for each of the 4 possible directions (l,r,u,d) unless at edge
    # 3) traverse graph
    # 4) stop once end node is reached (no need to finish graph)



    def hint_solution(self):
        #  perform first row as just sum
        for i in range(day15.cave.shape[0]-1):
            day15.cave[i+1, 0] += day15.cave[i,0]

        for j in range(day15.cave.shape[1]-1):
            day15.cave[0, j+1] += day15.cave[0,j]

        for k in range(1,np.min(day15.cave.shape)):
            day15.sum_row_col(k)

        return day15.cave[day15.cave.shape[0]-1, day15.cave.shape[1]-1]-day15.cave[0,0]

    # too slow
    # def recursion(self, data):
    #     total_right = 0
    #     total_down = 0
    #
    #     if ((data.shape[1] == 1) & (data.shape[0] == 1)):
    #         # print("ended", data[0,0])
    #         return data[0,0]
    #     elif data.shape[0] == 1:
    #         total_right = day15.recursion(data[:,1:])
    #         # print("right",total_right, data[0,0])
    #         return total_right + data[0,0]
    #     elif data.shape[1] == 1:
    #         total_down = day15.recursion(data[1:,:])
    #         # print("down",total_down, data[0,0])
    #         return total_down + data[0,0]
    #     else:
    #         total_right = day15.recursion(data[:,1:])
    #         total_down = day15.recursion(data[1:,:])
    #         # print("both have values", total_right, total_down)
    #         return data[0,0] + min(total_down, total_right)

    def solve(self):

        day15.max = 5
        day15.cave = day15.cave[:day15.max+1,:day15.max]
        print(day15.cave)

        start = pfc()
        total_idx = day15.hint_solution()
        # print(pfc() - start)


        print(day15.cave)
        return total_idx



#510 too high
day15 =Day15()
day15.get_data(False)
start = pfc()
solution_a = day15.solve()
# solution_b = day15.solve()
print(pfc()-start)