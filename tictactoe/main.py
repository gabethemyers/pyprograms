from win_tests import x_win, o_win

numbered_board = """
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |   
"""

board = """
      |     |     
   -  |  -  |  -  
 _____|_____|_____
      |     |     
   -  |  -  |  -  
 _____|_____|_____
      |     |     
   -  |  -  |  -  
      |     |   
"""

board = list(board)

location_indices = {1: 23, 2: 29, 3: 35, 4: 80, 5: 86, 6: 92, 7: 137, 8: 143, 9: 149}
matrix_locations = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}

matrix =[['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]

# introduction and explaination to game
tutornot = input('Welcome to tic tac toe!\nIf you would like a tutorial on how to play enter "tut" otherwise hit enter: ')
if tutornot == 'tut':
    print(numbered_board)
    print("Here is the locations for each square, when it is your turn enter that number and your marker will show up there")


played_sqaures = []
turn_count = 0
while turn_count < 9:
    print(''.join(board))
    if turn_count % 2 == 0:
        xs_choice = int(input("Player X's turn: "))
        while True:
            if xs_choice not in played_sqaures:
                break
            else:
                print("That square has already been played")
                xs_choice = int(input("Player X's turn: "))
        played_sqaures.append(xs_choice)
        board[location_indices[xs_choice]] = "X"
        matrix_location = matrix_locations[xs_choice]
        matrix[matrix_location[0]][matrix_location[1]] = 1
    elif turn_count % 2 == 1:
        os_choice = int(input("Player O's turn: "))
        while True:
            if os_choice not in played_sqaures:
                break
            else:
                print("That square has already been played")
                os_choice = int(input("Player O's turn: "))
        played_sqaures.append(os_choice)
        board[location_indices[os_choice]] = "O"
        matrix_location = matrix_locations[os_choice]
        matrix[matrix_location[0]][matrix_location[1]] = 0
    turn_count += 1
    if x_win(matrix):
        print("".join(board))
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f"Congratulations Player X you won in {turn_count} moves.")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        break
    if o_win(matrix):
        print("".join(board))
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f"Congratulations Player O you won in {turn_count} moves.")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        break


if turn_count > 8:
    print("".join(board))
    print("Looks like its a tie")

    
    


