import pandas as pd
import numpy as np
from helper_functions import Solution
DAY = 3


class DayThree_A(Solution):

    def get_data(self):
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            formatted_data = []
            data = f.readlines()
            for d in data:
                formatted_data.append(d.strip())

        for i,d in enumerate(formatted_data):
            formatted_data[i] = [int(x) for x in d]

        formatted_data = np.array(formatted_data)

        return formatted_data

    def solve(self):

        data = self.data

        totals = data.sum(axis=0)

        solution_gamma = [] # value with most
        solution_alpha = [] # values with least occurring
        for val in totals:
            if val > len(data)/2.:
                solution_gamma.extend([1])
                solution_alpha.extend([0])
            else:
                solution_gamma.extend([0])
                solution_alpha.extend([1])

        sa_int = ''.join([str(x) for x in solution_alpha])
        ga_int = ''.join([str(x) for x in solution_gamma])

        sa_int = int(sa_int, 2)
        ga_int = int(ga_int,2)
        self.solution = sa_int * ga_int


class DayThree_B(Solution):

    def get_data(self):
        print("Getting Data")
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            stripped_data = []
            data = f.readlines()
            for d in data:
                stripped_data.append(d.strip())

        self._data = stripped_data

    def format_data(self):
        print("Formatting data")
        # data = solution_a._data
        data = self._data
        for i, d in enumerate(data):
            data[i] = [int(x) for x in d]

        self._data = data

    def multiply_base2(self, o2, co2):
        self.solution = int(o2,2) * int(co2,2)

    def solve(self, data, partial_solution, flip):
        #  wants a list of lists containing integers

        # data = np.array(data)
        totals = np.array(data).sum(axis=0)

        if totals[0] >= len(data) / 2.:
            max_val = 1
            min_val = 0
        else:
            max_val = 0
            min_val = 1

        if flip:
            max_val = min_val

        # filter
        oxygen_list = []
        for i, d in enumerate(data):
            if d[0] == max_val:
                final_idx = i
                oxygen_list.append(d[1:])
            # else:
            #     co2_list.append(d[1:])
        if len(oxygen_list) == 0:
            return ("error")
        elif len(oxygen_list) == 1:
            #  get the last max value found that was removed from the list already
            partial_solution.extend([max_val])
            #  tack on whatever remaining part of the binary number is left to the end.
            partial_solution.extend(oxygen_list[0])
            if flip:
                self.co2 = "".join([str(x) for x in partial_solution])
            else:
                self.o2 = "".join([str(x) for x in partial_solution])
            return partial_solution
        else:
            partial_solution.extend([max_val])
            return self.solve(oxygen_list, partial_solution, flip)


solution_a = DayThree_A()
solution_b = DayThree_B()

solution_a._data = solution_a.get_data()
solution_a.solve()
solution_a.print_solution()
answer_a = solution_a.solution

#  possible bug, o2 could be co2 and co2 could be o2? For this problem it doesn't matter since they are reflections of one another
#  and they solve by multiply which is commutative.
solution_b.get_data()
solution_b.format_data()
co2 = solution_b.solve(solution_b.data, [], True)
o2 = solution_b.solve(solution_b.data, [], False)
solution_b.multiply_base2(solution_b.o2, solution_b.co2)
solution_b.print_solution()
answer_b = solution_b.solution


# def solve2(data,partial_solution, flip):
#     #  wants a list of lists containing integers
#
#     # data = np.array(data)
#     totals = np.array(data).sum(axis=0)
#
#     if totals[0] >= len(data) / 2.:
#         max_val = 1
#         min_val = 0
#     else:
#         max_val = 0
#         min_val = 1
#
#     if flip:
#         max_val = min_val
#
#     # filter
#     oxygen_list = []
#     for i, d in enumerate(data):
#         if d[0] == max_val:
#             final_idx = i
#             oxygen_list.append(d[1:])
#         # else:
#         #     co2_list.append(d[1:])
#     print(len(oxygen_list))
#     if len(oxygen_list) == 0:
#         return ("error")
#     elif len(oxygen_list) == 1:
#         print(data[final_idx], final_idx, partial_solution,"final run")
#         partial_solution.extend([max_val])
#         partial_solution.extend(oxygen_list[0])
#         return partial_solution
#     else:
#         partial_solution.extend([max_val])
#         return solve2(oxygen_list, partial_solution, flip)
#
#
# oxy_soln = []
# co2_soln = []
# oxy_soln =solve2(data, [], flip=False)
# co2_soln = str(solve2(data, [], flip=True))
# oxy_soln = '011010110111'
# co2_soln = '100101100000'
#
# int(oxy_soln,2) * int(co2_soln,2)

#  input data
#  find first digit that is maxed
#  filter
# recursive call using filtered data

