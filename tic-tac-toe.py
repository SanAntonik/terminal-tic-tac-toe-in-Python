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


# this function compeleted thanks to https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659#23294659
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
        print("\nThis position is already taken! Choose other values!")
        x = get_valid_input("\nEnter x value: ")
        y = get_valid_input("Enter y value: ")
        return check_position_availability(x, y)
    return (x, y)


def draw():
    spaces_count = 0
    for row in matrix:
        if " " in row:
            spaces_count += 1
    if spaces_count == 0:
        print("\nNo free space left. Draw.")
        return True
    return False  


# helper function of 'win'
def count_3s(kind_of_check, X_count, O_count):
    if X_count == 3:
        print(f"\nThere're 3 {kind_of_check} Xs. Player 1 won!")
        return True
    elif O_count == 3:
        print(f"\nThere're 3 {kind_of_check} Os. Player 2 won!")
        return True
    return False


def win():
    # horizontal check
    # for row in matrix:
    #     X_count = 0
    #     O_count = 0
    #     for elem in row:
    #         if elem == "X":
    #             X_count += 1
    #         elif elem == "O":
    #             O_count += 1

    for i in range(0, len(matrix)):
        X_count = 0
        O_count = 0
        for k in range(0, len(matrix)):
            if matrix[i][k] == "X":
                X_count += 1
            elif matrix[i][k] == "O":
                O_count += 1
        if count_3s("horizontal", X_count, O_count):
            return True

    # vertical check
    for i in range(0, len(matrix)):
        X_count = 0
        O_count = 0
        for k in range(0, len(matrix)):
            if matrix[k][i] == "X":
                X_count += 1
            elif matrix[k][i] == "O":
                O_count += 1
        
        if count_3s("vertical", X_count, O_count):
            return True        

    # diagonal check 
    # checking diagonal 0 0 - 1 1 - 2 2
    X_count = 0
    O_count = 0
    for i in range(0, len(matrix)):
        if matrix[i][i] == "X":
            X_count += 1
        elif matrix[i][i] == "O":
            O_count += 1
    if count_3s("diagonal", X_count, O_count):
        return True         

    # checking diagonal 0 2 - 1 1 - 2 0
    X_count = 0
    O_count = 0
    k = 2
    for i in range(0, len(matrix)):
        if matrix[i][k] == "X":
            X_count += 1
        elif matrix[i][k] == "O":
            O_count += 1
        k -= 1
    if count_3s("diagonal", X_count, O_count):
        return True     
    
    return False


matrix = [[" " for x in range(3)] for y in range(3)] 
print(grid(matrix))
for x in range(0, 10):

    p1_x, p1_y = check_position_availability(get_valid_input("\nPlayer 1, enter x value: "), get_valid_input("Player 1, enter y value: "))
    matrix[p1_x][p1_y] = "X"
    print(grid(matrix))

    if win():
        break

    if draw():
        break

    p2_x = get_valid_input("\nPlayer 2, enter x value: ")
    p2_y = get_valid_input("Player 2, enter y value: ")
    p2_x, p2_y = check_position_availability(p2_x, p2_y)
    print(p2_x, p2_y)
    matrix[p2_x][p2_y] = "O"
    print(grid(matrix))

    if win():
        break


