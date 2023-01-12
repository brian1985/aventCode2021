# This is a sample Python script.
import numpy as np
import re
import pandas as pd
import csv
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def get_data(problem_num):
    # data = np.genfromtxt("data\\prob"+str(problem_num)+".txt")
    # data = []
    #
    # with open("data\\day2.txt", mode='r') as f:
    #     reader = csv.reader(f, delimiter=' ')
    #
    #     for row in reader:
    #         data.append(row)

    df = pd.read_csv(f"data\\prob{problem_num}.txt",sep=' ')

    return df


def convert_dtypes(data):
    results = [[x[0], int(x[1])] for x in data]


def problem_1(data):
    result = np.sum(data[1:]- data[:-1] > 0)
    return result


def problem_2(data):
    n=0
    rolling_sum = np.zeros(len(data)-2)
    for n in np.arange(0,len(data) - 2):
        rolling_sum[n] = np.sum(data[n:n+3])

    return problem_1(rolling_sum)


def problem_3(data):
    results = data.groupby('direction').sum()
    results_final = (-results.loc['up','amount'] + results.loc['down','amount'])*results.loc['forward','amount']

    return results_final


def problem_4(data):
    x = 0
    depth = 0
    aim = 0

    for direction, amount in data.values:
        amount = int(amount)
        if 'forward' in direction:
            x += amount
            depth += aim*amount
        elif 'down' in direction:
            aim += amount
        elif 'up' in direction:
            aim -= amount
        else:
            print("failed")

    result_final = x*depth

    return result_final


def problem_5(data):
    pass


def problem_6(data):
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = get_data(1)
    answer1 = problem_1(data)

    #  data for problem 2 = data for problem 1
    data = get_data(1)
    answer2 = problem_2(data)

    data = get_data(3)
    answer3 = problem_3(data)

    data = get_data(3)
    answer4 = problem_4(data)

    data = get_data(5)
    answer5 = problem_5()

    data = get_data(5)
    answer6 = problem_6()

# See PyCha
# rm help at https://www.jetbrains.com/help/pycharm/
