# 102architect

Geometric transformations and homogeneous coordinates.

Project for semester 1 of the Epitech Math module.

### Description

This project involves developing a program to calculate the coordinates of a point after applying various geometric transformations. You will implement transformations like translation, scaling, rotation, and reflection using homogeneous coordinates without relying on external matrix calculus libraries like numpy.

## Getting Started

### Dependencies

- [Python3](https://python.org/)

### Installation

* Download/Clone the repository and enter its directory
* Now you are ready to run the code

## Usage
- **Execution**: `./102architect x y transfo1 arg1 [arg2] [transfo2 arg21 [arg22]] ...`

### Arguments
- **`x`**: abscissa of the original point
- **`y`**: ordinate of the original point
- **`transfo arg1 [arg2]`**: transformation to be applied:
- **`-t i j`**: translation along vector `(i, j)`
- **`-z m n`**: scaling by factors `m` (x-axis) and `n` (y-axis)
- **`-r d`**: rotation centered at O by a `d` degree angle
- **`-s d`**: reflection over the axis passing through O with an inclination angle of `d` degrees

## Acknowledgments

* [Epitech](https://www.epitech.eu/)

## Authors
* **Daniel Sanchez** ([GitHub](https://github.com/angsanch) / [LinkedIn](https://www.linkedin.com/in/angeldanielsanchez/))
* **Sofia Martin** ([GitHub](https://github.com/sofiampx))

## License
This project is licensed under the GNU Public License version 3.0 - see the [LICENSE](LICENSE) file for details.
