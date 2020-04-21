# Реализовать некий класс Matrix, у которого:
# 1. Есть собственный конструктор, который принимает в качестве аргумента - список списков, копирует его
# (то есть при изменении списков, значения в экземпляре класса не должны меняться). Элементы списков гарантированно
# числа, и не пустые.
# 2. Метод size без аргументов, который возвращает кортеж вида (число строк, число столбцов).
# 3. Метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует
# экземпляр класса Matrix)
# 4. На основе пункта 3 сделать метод класса create_transposed, который будет принимать на вход список списков,
# как и в пункте 1, но при этом создавать сразу транспонированную матрицу.
import copy


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
