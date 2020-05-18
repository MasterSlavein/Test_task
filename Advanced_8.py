# 1. Реализовать подсчёт елементов в классе Matrix с помощью collections.Counter.
# Можно реализовать протоколом итератора и тогда будет такой вызов - Counter(maxtrix). Либо сделать какой-то
# метод get_counter(), который будет возвращать объект Counter и подсчитывать все элементы внутри матрицы.
# Какой метод - ваш выбор.

# 2. Используя модуль unittests написать тесты: сложения двух матриц, умножения матрицы и метод transpose

import copy
from collections import Counter


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = copy.deepcopy(list_of_lists)

    def size(self):
        number_of_rows = len(self.matrix)
        number_of_columns = len(self.matrix[0])
        size_of_matrix = (number_of_rows, number_of_columns)
        return size_of_matrix

    def transpose(self):
        trans_matrix = list(zip(*self.matrix))
        self.matrix = trans_matrix
        return self

    @classmethod
    def create_transposed(cls, list_of_lists):
        instance = cls(list_of_lists)
        return instance.transpose()

    def __add__(self, other):
        if self.size() == other.size():
            resulted_matrix = []
            for new_list in zip(self.matrix, other.matrix):
                rows = []
                for elements in zip(new_list[0], new_list[1]):
                    rows.append(sum(elements))
                resulted_matrix.append(rows)
            return resulted_matrix
        else:
            raise ValueError(f"Matrices have different sizes - Matrix #1 {self.size()} and Matrix #2 {other.size()}")

    def __mul__(self, scalar):
        resulted_matrix = []
        for row in self.matrix:
            rows = []
            for column in row:
                rows.append(column * scalar)
            resulted_matrix.append(rows)
        return resulted_matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % column for column in row]) for row in self.matrix])

    def get_counter(self):
        counter_object = Counter()
        for rows in self.matrix:
            counter_object += Counter(rows)
        return counter_object


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[1, 2, 3], [4, 5, 6]])

print(a + b, a * 2)
print(a.__add__(b))
print(a.__mul__(2))
print(a.__str__())
print(a.get_counter())
