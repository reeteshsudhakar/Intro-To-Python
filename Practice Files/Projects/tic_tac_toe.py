
# board display

def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])



# player input

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("P1, please pick a side, X or O: ").upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')



# board positioning

def place_marker(board, marker, position):
    board[position] = marker



# win conditions

def winner_check(board, mark):
    return (
        # top across 
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        # middle across
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        # bottom across
        (board[7] == mark and board[8] == mark and board[9] == mark) or 
        # left down
        (board[1] == mark and board[4] == mark and board[7] == mark) or 
        # middle down
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        # right down
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        # diagonal down, left to right
        (board[1] == mark and board[5] == mark and board[9] == mark) or 
        # diagonal down, right to left
        (board[3] == mark and board[5] == mark and board[7] == mark)
    )



# who goes first
import random 
  
def choosing_first():
    if random.randint(0,1) == 0:
        return "P1"
    else:
        return "P2"



# placing items on board

def space_free_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_free_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_free_check(board, position):
        position = int(input('Choose your next position from 1-9:  '))
    return position



# playing again

def replay():
    replay_game = ''
    while replay_game.lower() != 'yes' and replay_game.lower() != 'no':
        replay_game = input('Do you want to play again? Enter Yes or No: ')
    return replay_game[0].lower().startswith('y')


# connecting everything woooo

print("WELCOME TO TIC TAC TOE. LET'S GET STARTED!")

while True:
    zeBoard = [' '] * 10
    print('''THESE ARE THE POSITIONS ON THE BOARD:
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    ''') 
    P2_marker, P1_marker = player_input()
    turn = choosing_first()
    print(turn + " will go first!")

    play_the_game = input("Are you ready to play? Yes or No: ")

    if play_the_game.lower().startswith('y'):
        start_game = True
    else:
        start_game = False

    while start_game == True:
        if turn == "P1":
            display_board(zeBoard)
            position = player_choice(zeBoard)
            place_marker(zeBoard, P1_marker, position)

            if winner_check(zeBoard, P1_marker):
                display_board(zeBoard)
                print("P1 HAS WON THE GAME!")
                start_game = False
            else:
                if full_board_check(zeBoard):
                    display_board(zeBoard)
                    print("There is no winner - this is a draw!")
                    break
                else:
                    turn = "P2"
        else:
            display_board(zeBoard)
            position = player_choice(zeBoard)
            place_marker(zeBoard, P2_marker, position)

            if winner_check(zeBoard, P2_marker):
                display_board(zeBoard)
                print('P2 HAS WON THE GAME!')
                start_game = False
            else:
                if full_board_check(zeBoard):
                    display_board(zeBoard)
                    print('There is no winner - this is a draw!')
                    break
                else:
                    turn = 'P1'

    if not replay():
        break


    
