import math
import numpy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.determ = 0

    def print_matrix(self):
        for i in self.matrix:
            print(i)

    def get_determinant(self):
        self.determ = numpy.linalg.det(self.matrix)
        return self.determ

    def __lt__(self, other):  # x < y
        print("Enter LT")
        if self.get_determinant() < other.get_determinant():
            return True
        else:
            return False

    def __le__(self, other):  # x ≤ y
        print("Enter LE")
        if self.get_determinant() <= other.get_determinant():
            return True
        else:
            return False

    def __eq__(self, other):  # x == y
        if self.get_determinant() == other.get_determinant():
            return True
        else:
            return False

    def __ne__(self, other):  # x != y
        if self.get_determinant() != other.get_determinant():
            return True
        else:
            return False

    def __gt__(self, other):  # x > y
        if self.get_determinant() > other.get_determinant():
            return True
        else:
            return False

    def __ge__(self, other):  # x ≥ y
        if self.get_determinant() >= other.get_determinant():
            return True
        else:
            return False

    def __add__(self, other):  # x + y
        result = [map(sum, zip(*i)) for i in zip(self.matrix, other.matrix)]
        return result

    def __mul__(self, other):  # x * y
        result = numpy.dot(self.matrix, other.matrix)
        return result


matr1 = [[2, 4],
        [5, 6]]

matr2 = [[2, 5],
        [3, 7]]

print("matrix 1:")
matrix_1 = Matrix(matr1)
matrix_1.print_matrix()
print(matrix_1.get_determinant())
matrix_2 = Matrix(matr2)
print("matrix 2:")
matrix_2.print_matrix()
print(matrix_2.get_determinant())

if matrix_1 < matrix_2:
    print("Ok")

