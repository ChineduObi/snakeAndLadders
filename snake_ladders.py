""" This is a nested list representing a game board grid.
The grid consists of multiple rows and columns, with each cell
containing either a number or a tuple with two additional 
elements (symbol and value). """
grid = [[[25],[26], [27,'S', 1], [28], [29], [30] ],
        [[24],[23], [22], [21,'S',9],[20,'L',29],[19,'S',7]],
        [[13],[14], [15], [16], [17,'S',4], [18] ],
        [[12],[11,'L',26],[10], [9], [8], [7] ],
        [[1], [2], [3,'L',22], [4], [5,'L',8], [6] ]]



""" This function board_position takes a nested list 
(mylist) and a number (num) as input. 
It iterates through the list and checks if the number exists in the inner lists.
If found, it returns the index of the outer list, index of the inner list, 
index of the number, and the length of the inner list. 
If the number is not found, it raises a ValueError with a corresponding message. """
def board_position(mylist, num):
    for index, sub_list in enumerate(mylist):
        for inner_list in sub_list:
            if num in inner_list and inner_list.index(num) == 0:
                return index, sub_list.index(inner_list), inner_list.index(num), len(inner_list)
    raise ValueError("'{num}' is not in list".format(num=num))

""" This function request_input prompts the user to input a value between 1 and 6.
It checks if the input is within the valid range and
if the sum of the current position and input is less than or equal to 30. 
If both conditions are met, it returns the user input.
If the input is 'exit', it returns -1. Otherwise, it returns 0. """
def request_input(grid, current_pos):
    userInput = int(input("Input a value between 1 and 6: "))

    if (1 <= userInput <= 6) and ((current_pos+userInput) <= 30):
        return userInput

    elif (1 <= userInput <= 6) and ((current_pos+userInput) <= 30):
        return 0

    elif str(userInput).lower() == 'exit':
        return -1
    
    else:
        return 0

""" This function make_move updates the current position based on the number of moves. 
It adds the moves value to the current_pos.
Then, it calls the board_position function to determine the new position on the grid. 
If the length of the inner list at the new position is 3 and the symbol is 'L',
it prints "Hooray!!!" and updates the current_pos to the value specified in the tuple. 
If the length is 3 and the symbol is 'S', 
it prints "Oops!!!" and updates the current_pos to the value specified in the tuple.
Otherwise, it returns the updated current_pos. """
def make_move(grid, current_pos, moves):
    current_pos+=moves
    decide = board_position(grid, current_pos)
    if decide[3] == 3 and (grid[(decide[0])][decide[1]][1] == "L"):
        print("Hooray!!!")
        current_pos = grid[(decide[0])][decide[1]][2]
        return current_pos
    elif decide[3] == 3 and (grid[(decide[0])][decide[1]][1] == "S"):
        print("Oops!!!")
        current_pos = grid[(decide[0])][decide[1]][2]
        return current_pos
    else: 
        return current_pos

""" This function convert_grid takes the grid as input and 
converts it to a new grid where each cell contains either a number or the first element of a list. 
It iterates over each row and cell, checks if the cell is a list, 
and appends either the number or the first element of the list to the converted_row. 
Finally, it adds the converted_row to the converted_grid and returns the updated grid. """
def convert_grid(grid):
    converted_grid = []

    for row in grid:
        converted_row = []
        for cell in row:
            if isinstance(cell, list):
                converted_row.append(cell[0])
            else:
                converted_row.append(cell)
        converted_grid.append(converted_row)

    return converted_grid

""" This function display_grid takes the grid and pos (current position) as input. 
It calls the convert_grid function to get the converted grid.
Then, it iterates over each row and cell in the grid and prints them with "|" separators.
If the cell value is equal to the pos, it prints "*" to indicate the current position. 
Finally, it prints a new line to move to the next row. """
def display_grid(grid, pos):
    grid = convert_grid(grid)
    for row in grid:
        print("|", end="")
        for cell in row:
            if cell == pos:
                print("*|", end="")
            else:
                print(str(cell) + "|", end="")
        print()


""" This function play_game is the main game loop. 
It initializes the gameContinue flag and the current_pos to 1. 
Then, it displays the grid using the display_grid function. 
The game continues in a loop until the gameContinue flag is set to False. 
Within the loop, it takes user input using the request_input function. 
If the input is neither 0 nor -1, it calls the make_move function to update the current_pos. If the input is 0,
it prompts the user for a valid response again. If the input is -1, the game ends. 
After each move, it displays the updated grid.
If the current_pos reaches 30, it prints "Congratulations, you won!" and ends the game. """
def play_game(grid):
    gameContinue = True
    current_pos = 1
    display_grid(grid, current_pos)

    while (gameContinue):
        userInput = request_input(grid, current_pos)
        if (userInput != 0) or (userInput != -1):
            make_move(grid, current_pos, userInput)


        elif userInput == 0:
            print("Invalid Response, Try again!!")
            userInput = request_input(grid, current_pos) 

        else:
            break
        
        current_pos = make_move(grid, current_pos, userInput)


        display_grid(grid, current_pos)

        if current_pos == 30:
            print("Congratulations, you won!")
            gameContinue = False
        
        else:
            gameContinue = True


   
        
""" This line starts the game by calling
the play_game function with the grid as the input. """
play_game(grid)


