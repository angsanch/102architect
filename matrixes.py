##
## EPITECH PROJECT, 2023
## matrixes.py
## File description:
## manage matrixes
##

class Matrix:
    matrix:list
    width:int
    height:int
    def __init__(self, width, height, numbers):
        if type(width) != int or type(height) != int or type(numbers) != list:
            raise TypeError("Error, invalid type for dimensions")
        if width * height != len(numbers):
            raise ValueError("Invalid amount of numbers")
        try:
            numbers = [float(i) for i in numbers]
        except ValueError:
            raise TypeError("Invalid numbers inputted")
        self.width = width
        self.height = height
        self.matrix = []
        for i in range(height):
            self.matrix.append(numbers[width * i:width * (i + 1)])

    def _check_matrix(matrix):
       if not isinstance(matrix, Matrix):
            raise TypeError("You can only add other matrixes to a matrix")

    def _check_same_size(self, matrix):
       if self.width != matrix.width or self.height != matrix.height:
            raise ValueError("Matrixes must be the same size")

    def _check_mul_compatible(self, matrix):
        if self.width != matrix.height:
            raise ValueError("Incompatible matrix sizes")

    def __add__(self, this):
        Matrix._check_matrix(this)
        self._check_same_size(this)
        result = []
        for i in range(self.height):
            result += [self.matrix[i][j] + this.matrix[i][j]
                for j in range(self.width)]
        return Matrix(self.width, self.height, result)

    def __sub__(self, this):
        Matrix._check_matrix(this)
        self._check_same_size(this)
        result = []
        for i in range(self.height):
            result += [self.matrix[i][j] - this.matrix[i][j]
                for j in range(self.width)]
        return Matrix(self.width, self.height, result)

    def __mul__(self, this):
        Matrix._check_matrix(this)
        self._check_mul_compatible(this)
        result = []
        for i in range(self.height):
            for j in range(this.width):
                result.append(combine_lists(self.matrix[i],
                    [k[j] for k in this.matrix]))
        return Matrix(self.height, this.width, result)

    def __repr__(self):
        lines = ["\t".join([f"{0 if round(j, 2) == 0 else j:.2f}" for j in i])
            for i in self.matrix]
        return "\n".join(lines)


def combine_lists(l1, l2):
    if len(l1) != len(l2):
        raise IndexError("Lists need to be the same size")
    result = 0
    for i in range(len(l1)):
        result += l1[i] * l2[i]
    return result
