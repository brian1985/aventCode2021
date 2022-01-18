import numpy as np
DAY = 7


#  Fuel consumption of crabs
class Day7():

    def __init__(self):
        self.data = None

    def get_data(self):
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            ages = f.read()
            ages = [int(age) for age in ages.split(',')]
            self.data = np.array(ages)

    def sum_first_n_int(self, n):
        return n*(n+1)/2

    def solve(self, is_part_a):
        # self.data = np.array([16,1,2,0,4,2,7,1,2,14,5,5,5,5,5,5,5,5,5])
        if is_part_a:
            self.mn = np.median(self.data)
            self.fuel_burns = np.abs(self.data - self.mn)
            fuel_cost = self.fuel_burns.sum()

        else:
            self.mn = np.mean(self.data)
            fuel_burns_floor = np.abs(self.data - np.floor(self.mn))
            fuel_burns_ceil = np.abs(self.data - np.ceil(self.mn))
            fuel_cost_floor = np.apply_along_axis(lambda n: self.sum_first_n_int(n),0, fuel_burns_floor).sum()
            fuel_cost_ceil = np.apply_along_axis(lambda n: self.sum_first_n_int(n),0, fuel_burns_ceil).sum()
            fuel_cost = np.min([fuel_cost_ceil, fuel_cost_floor])



        # sum of first n integers
        # uses formula by Gauss
        # fuel_cost = n * (n+1) / 2


        return fuel_cost, self.mn

day7 =Day7()
day7.get_data()
solution_a = day7.solve(True)

336120

day7 =Day7()
day7.get_data()
solution_b = day7.solve(False)
print(solution_b)



#  solution found using monte carlo.
#  solution courtesy of 'cramur' on reddit thread for solution
#  Good opportunity to refresh memory on this technique
#  evn though this approach is grossly inefficient. Better would be brute force.

def p_monte(initial):
    positions = list(map(int, initial.split(',')))
    low, high = min(positions), max(positions)
    min_pos = np.median(positions)
    min_cost = sum(np.abs(pos1-min_pos)*(np.abs(pos1-min_pos)+1)/2 for pos1 in positions)

    for _ in range(10000):
        projected_min_pos = np.random.randint(low, high)

        new_cost = sum(abs(pos1 - projected_min_pos)*(abs(pos1 - projected_min_pos) + 1)/2 for pos1 in positions)
        if new_cost < min_cost:
            min_cost = new_cost
    return min_cost


with open(f"data\\day7.txt", mode='r') as f:
    ages = f.read()
    initial = ages
cost = p_monte(ages)