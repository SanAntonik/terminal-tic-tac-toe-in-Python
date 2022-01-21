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

# thanks to https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659#23294659
def get_valid_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("\nINVALID INPUT!\nYou can only pass integers from 0 to 2")
            continue

        if value < 0 or value > 2:
            print("\nINVALID INPUT!\nYou can only pass integers from 0 to 2")
            continue
        else:
            break
    return value

p1_x = get_valid_int_input("\nEnter x value: ")
print(p1_x)