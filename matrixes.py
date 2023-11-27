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
            raise ValueError("Invalid amount of numbers.")
        try:
            numbers = [float(i) for i in numbers]
        except ValueError:
            raise TypeError("Invalid numbers inputted")
        self.width = width
        self.height = height
        self.matrix = []
        for i in range(height):
            self.matrix.append(numbers[width * i:width * (i + 1)])

if __name__ == "__main__":
    print(Matrix(4, 3, [1, "a.d", 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).matrix)
