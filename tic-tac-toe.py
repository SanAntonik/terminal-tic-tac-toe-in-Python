import numpy as np

matrix = [["X" for x in range(3)] for y in range(3)] 

print(matrix)


def grid(matrix, sep="|"):
    print(f"\n{23 * sep}")
    for row in range(len(matrix)):
        print(f"{sep}{sep}     {sep}{sep}     {sep}{sep}     {sep}{sep}")
        for column in range(len(matrix[row])):
            print(f"{sep}{sep}  {matrix[row][column]}  ", end="")
        print(f"{sep}{sep}")
        print(f"{sep}{sep}     {sep}{sep}     {sep}{sep}     {sep}{sep}")
        print(f"{23 * sep}")
    return "Current grid"

print(grid(matrix))