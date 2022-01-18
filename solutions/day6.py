import pandas as pd
import numpy as np
from helper_functions import Solution
DAY = 6

#  exponential fish growth
class Day6():
    permutations = [1,2,3,4,5,6,0]
    def __init__(self, max_days):
        self.MAX_DAYS = max_days
    def get_data(self):
        day6.data = list(7*[0])
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            ages = f.read()
            for age in ages.split(','):
                day6.data[int(age)] += 1
            # day6.ages, day6.data = np.unique(ages, return_counts=True)

    def format_data(self):
        self.data = np.ulonglong(day6.data)

    def permute(self):
        day6.data = day6.data[day6.permutations]


    def generate_new_fish(self, new_fish):
        day6.young_fish[1] = new_fish

    def permute_young_fish(self):
        day6.data[6] += day6.young_fish[0]
        day6.young_fish[0] = day6.young_fish[1]
        day6.young_fish[1] = 0

    def solve(self):
        day6.young_fish = np.ulonglong([0,0])
        for day in range(0,self.MAX_DAYS):
            new_fish = day6.data[0]
            self.permute()
            self.permute_young_fish()
            self.generate_new_fish(new_fish)

        count_fish = day6.young_fish.sum() + day6.data.sum()
        return count_fish

day6 =Day6(80)
day6.get_data()
day6.format_data()
solution_a = day6.solve()

389726

day6 =Day6(256)
day6.get_data()
day6.format_data()
solution_b = day6.solve()
print(solution_b)