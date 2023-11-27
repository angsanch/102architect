##
## EPITECH PROJECT, 2023
## transforms.py
## File description:
## Matrix creation functions
##

from matrixes import Matrix
import math

def get_rads(num):
    return math.radians(num)

def translation(i, j):
    print(f"Translation along vector ({i}, {j})")
    return Matrix(3, 3, [
        1, 0, i,
        0, 1, j,
        0, 0, 1])

def scaling(m, n):
    print(f"Scaling by factors {m} and {n}")
    return Matrix(3, 3, [
        m, 0, 0,
        0, n, 0,
        0, 0, 1])

def rotation(d, _):
    print(f"Rotation by a {d} degree angle")
    rad = get_rads(d)
    return Matrix(3, 3, [
        math.cos(rad), -math.sin(rad), 0,
        math.sin(rad), math.cos(rad), 0,
        0, 0, 1])

def reflection(d, _):
    print(f"Reflection over an axis with an inclination angle of {d} degrees")
    rad = get_rads(d)
    return Matrix(3, 3, [
        math.cos(2 * rad), math.sin(2 * rad), 0,
        math.sin(2 * rad), -math.cos(2 * rad), 0,
        0, 0, 1])

transforms = {"t": translation,
                    "z": scaling,
                    "r": rotation,
                    "s": reflection}
