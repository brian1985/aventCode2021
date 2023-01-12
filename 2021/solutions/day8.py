import numpy as np
import re
from time import perf_counter as pfc

DAY = 8


#  Fuel consumption of crabs
class Day8():

    def __init__(self):
        self.data = None

    def get_data(self):
        with open(f"data\\day{DAY}.txt", mode='r') as f:
            self.digits = f.readlines()
            self.input = []
            self.output = []
            for line in self.digits:
                ten_digits, output_digits = line.strip().split(' | ')
                self.input.append(ten_digits)
                self.output.append(output_digits)

    def solve_input(self, digits):
        # find the easy ones: 1,4,7,8
        match = re.findall(r"\b\w{2,2}\b", digits)[0]
        n_one = set(match)
        n_eight = set(re.findall(r"\b\w{7,7}\b", digits)[0])
        n_four = set(re.findall(r"\b\w{4,4}\b", digits)[0])
        n_seven = set(re.findall(r"\b\w{3,3}\b", digits)[0])

        # next solve length 5 numbers.
        # it is noted that since order isn't important a set might help
        # also, using set logic, the set difference between 3 and 1 set(3).diff(set(1)) is length 2
        # this can be done for each of the remaining numbers finding combinations that give a unique difference
        # this solves the input.
        # output is then solved by matching the sets so there is no difference.
        matches = re.findall(r'\b\w{5,5}\b', digits)
        for m in matches:
            if len(set(m).difference(n_one)) == 3:
                n_three = set(m)
            elif len(set(m).difference(n_four)) == 2:
                n_five = set(m)
            else:
                n_two = set(m)

        matches = re.findall(r'\b\w{6,6}\b', digits)
        for m in matches:
            if len(set(m).difference(n_one)) == 5:
                n_six = set(m)
            elif len(set(m).difference(n_three)) == 1:
                n_nine = set(m)
            else:
                n_zero = set(m)

        return [n_zero, n_one, n_two, n_three, n_four, n_five, n_six, n_seven, n_eight, n_nine]

    def solve_output(self, output, in_soln):
        number = 4 * [0]
        for idx, d in enumerate(output):
            for val, s in enumerate(in_soln):
                if (len(set(d).difference(s)) == 0) & (len(set(d)) == len(s)):
                    number[idx] = val

        return number

    def solve(self):
        # solution_a
        count = 0
        for i in day8.output:
            count += len(re.findall(r"\b(\w{2,4}|\w{7,7})\b", i))

        # solution_b
        results = []
        for i_idx, i in enumerate(day8.input):

            in_dig = day8.solve_input(i)
            number = day8.solve_output(day8.output[i_idx].split(' '), in_dig)
            results.append(1000*number[0] + 100 * number[1] + 10 * number[2] + number[3])

        return count, np.array(results).sum()

    def solve_b(self):
        pass



#1061
day8 =Day8()
day8.get_data()
start = pfc()
solution_a, solution_b = day8.solve()
print(pfc()-start)




# approach using segment level details instead of len -> number level
from collections import Counter



with open("data\\day8.txt") as f:
    digits = f.readlines()

digits = [(digit.split("|")[0].strip(), digit.split("|")[1].strip()) for digit in digits]
start = pfc()

seven_seg = {"abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
    }

total = 0

def match_length(counter, match):
    output = {k for k,v in counter.items() if v == match}
    return output

for display in digits:
    output = ""
    key = Counter(display[0])
    key_len_dict = {len(key): key for key in display[0].split()}
    del key[" "]
    key_rev = {v: k for k,v in key.items()}
    translation = {}
    p_8 = match_length(key, 8)
    p_7 = match_length(key, 7)
    one = {k for k in key_len_dict[2]}
    four = {k for k in key_len_dict[4]}
    translation['b'] = key_rev[6]
    translation['e'] = key_rev[4]
    translation['f'] = key_rev[9]
    translation['c'] = ''.join(p_8 & one) # P8 and in 1 == c
    translation['a'] = ''.join(p_8 - one) # P8 and not in 1 == a
    translation['d'] = ''.join(p_7 & four) # P7 and in 4 == d
    translation['g'] = ''.join(p_7 - four) # P7 and not in 4 == g
    translation_2 = {v: k for k, v in translation.items()}

    output_value = ""
    for number in display[1].split():
        translated = "".join(sorted([translation_2[n] for n in number]))
        print(f"{number} -> {translated} -> {seven_seg[translated]}")
        output_value += str(seven_seg[translated])

    total += int(output_value)

print(f"{total=}")
print(pfc()-start)
