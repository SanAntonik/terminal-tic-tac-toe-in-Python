import numpy as np

matrix = [[" " for x in range(3)] for y in range(3)] 

# print(matrix)


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
# we're looking for an integer from 0 to 2. Other values won't pass.
def get_valid_input(prompt):
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


def check_position_availability(x, y):
    if matrix[x][y] != " ":
        print("This position is already taken! Choose other values!")
        x = get_valid_input("\nEnter x value: ")
        y = get_valid_input("Enter y value: ")
        return check_position_availability(x, y)
    return (x, y)
    

# if "X" in matrix:
#     print("X is here")

for x in range(0, 10):
    p1_x, p1_y = check_position_availability(get_valid_input("\nPlayer 1, enter x value: "), get_valid_input("Player 1, enter y value: "))
    print(p1_x, p1_y)
    matrix[p1_x][p1_y] = "X"
    print(grid(matrix))

    p2_x = get_valid_input("\nPlayer 2, enter x value: ")
    p2_y = get_valid_input("Player 2, enter y value: ")
    p2_x, p2_y = check_position_availability(p2_x, p2_y)
    print(p2_x, p2_y)
    matrix[p2_x][p2_y] = "O"
    print(grid(matrix))


# if "X" in matrix:
#     print("X is here")

# p2_x = get_valid_input("\nPlayer 2, enter x value: ")
# p2_y = get_valid_input("Player 2, enter y value: ")
# print(check_position_availability(p2_x, p2_y))
# matrix[p2_x][p2_y] = "O"

# print(grid(matrix))