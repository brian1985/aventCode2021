import numpy as np
import re
from collections import deque, Counter


def get_input():
    with open("2022/input06.txt") as f:
        return f.read()


def p1(input, num_distinct):
    for i in range(len(input)):
        if len(set(input[i:i+num_distinct])) == num_distinct:
            return i+num_distinct

file_input = get_input()
results4 = p1(file_input,4)
results14 = p1(file_input,14)
