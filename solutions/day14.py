import numpy as np
import re
from time import perf_counter as pfc

DAY = 14


#  Polymer chain to improve submarine durability
class Day14():

    def __init__(self):
        self.data = None

    def get_data(self):
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            day14.polymer = f.readline().strip()
            mappings = [(line.strip().split(" -> ")) for line in f.readlines()]

            day14.mappings = dict()
            for k,v in mappings:
                day14.mappings[k] = v


    def init_polymer_dict(self):
        day14.counts = dict()
        #  init the counts
        for idx, ch in enumerate(day14.polymer[:-1]):
            day14.counts[day14.polymer[idx:idx + 2]] = day14.counts.get(day14.polymer[idx:idx + 2], 0) + 1


    def get_middle_element(self, key):
        return day14.mappings[key]


    def update_element_counts(self,keys):
        #element is the new middle character to add
        #left_key and right_key are the new left 2 and right 2 char of a 3 char string
        #  if key appears 4 times, then I need to add the l and r keys 4 times
        #  X times is current val of counts (without update-need temp)
        temp_dict = dict()

        for k in keys:
            element = day14.get_middle_element(k)
            left_key = k[0] + element
            right_key = element + k[1]
            insertions = day14.counts.get(k, 0) #  day14[k] is the times the key appears currently
            temp_dict[left_key] = temp_dict.get(left_key,0) + insertions
            temp_dict[right_key] = temp_dict.get(right_key,0) + insertions

        #  now that all updates have occurred, we can assign the result to our dict
        day14.counts = temp_dict.copy()  # make sure changes to temp_dict doesn't change counts.



    def solve(self, iterations):
        day14.init_polymer_dict()

        for i in range(iterations):
            day14.update_element_counts(day14.counts.keys())

        #  dict that takes double char keys to single char keys
        day14.final_counts = dict()

        for k in day14.counts:
            for ch in k:
                #  divide 2 because of double counting (except first and last element of original polymer)
                day14.final_counts[ch] = day14.final_counts.get(ch,0) + day14.counts[k]/2

        day14.final_counts[day14.polymer[0]] += 0.5
        day14.final_counts[day14.polymer[len(day14.polymer)-1]] += 0.5

        diff = np.array(list(day14.final_counts.values())).max() - np.array(list(day14.final_counts.values())).min()
        return diff




#2174 too low
day14 =Day14()
day14.get_data()
start = pfc()
solution_a = day14.solve(10)
solution_b = day14.solve(40)
print(pfc()-start)