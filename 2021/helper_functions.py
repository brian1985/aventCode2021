import pandas as pd
import abc

class Solution(abc.ABC):
    def __init__(self):
        self._data = None
        self._solution = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value=[1,None]):
        """

        :param value: tuple of day and line of 'header or None'
        :return: None
        """
        day = value[0]
        has_header = value[1]
        self._data = pd.read_csv(f"data\\day{day}.txt", sep=' ', header=has_header, dtype='object')

    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, solution):
        self._solution = solution

    def print_solution(self):
        print(self.solution)

    @abc.abstractmethod
    def solve(self):
        pass