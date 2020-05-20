# 1. Реализовать подсчёт елементов в классе Matrix с помощью collections.Counter.
# Можно реализовать протоколом итератора и тогда будет такой вызов - Counter(maxtrix). Либо сделать какой-то
# метод get_counter(), который будет возвращать объект Counter и подсчитывать все элементы внутри матрицы.
# Какой метод - ваш выбор.

# 2. Используя модуль unittests написать тесты: сложения двух матриц, умножения матрицы и метод transpose
import unittest
from Advanced_8 import Matrix


class TestMatrix(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.matrix = Matrix([[1, 2, 3], [4, 5, 6]])

    # Each test method starts with the keyword test_
    def test_add(self):
        matrix_b = [[1, 2, 3], [4, 5, 6]]
        matrix_c = [[2, 4, 6], [8, 10, 12]]
        self.assertEqual(self.matrix.__add__(matrix_b), matrix_c)

    def test_multiply(self):
        matrix_a = [[1, 2, 3], [4, 5, 6]]
        matrix_c = [[2, 4, 6], [8, 10, 12]]
        self.assertEqual(self.matrix.__mul__(2), matrix_c)

    def test_transpose(self):
        matrix_a = [[1, 2, 3], [4, 5, 6]]
        transpose_a = [(1, 4), (2, 5), (3, 6)]
        self.assertEqual(self.matrix.transpose(), transpose_a)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
