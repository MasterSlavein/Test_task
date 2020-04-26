# К реализованному классу Matrix в Домашнем задании 3 добавить следующее:
# 1. __add__ принимающий второй экземпляр класса Matrix и возвращающий сумму матриц, если передалась на вход матрица
# другого размера - поднимать исключение MatrixSizeError (по желанию реализовать так, чтобы текст ошибки содержал
# размерность 1 и 2 матриц - пример: "Matrices have different sizes - Matrix(x1, y1) and Matrix(x2, y2)")
# 2. __mul__ принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр/
# 3. __str__ переводящий матрицу в строку. Столбцы разделены между собой табуляцией, а строки — переносами
# строк (символ новой строки). При этом после каждой строки не должно быть символа табуляции и в конце не должно быть
# переноса строки.
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
