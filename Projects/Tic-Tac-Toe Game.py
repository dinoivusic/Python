import random
# printing out a board
def board_display(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

sample_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

print(board_display(sample_board))
#asking for player marker
def player_input():
    mark = ''
    while mark != 'X' and mark != 'O':
        mark = input('Player one please select X or O').upper()

    if mark == 'X':
        return('X','O')
    else:
        return('O', 'X')


print(player_input())
# assigning a marker to aa certain position on the board
def place_the_marker(board,position,mark):
    board[position] = mark

print(place_the_marker(sample_board,8,'$'))
print(board_display(sample_board))
#check if someone won
def check_for_win(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

print(check_for_win(sample_board,'O'))

# who is playing first
def plays_first():
    num = random.randint(1,2)
    if num == 1:
        return 'Player 1 goes first'
    else:
        return 'Player 2 goes first'

print(plays_first())

#checking if all the positions are filled
def check_space(board, position):
    return board[position] == ' '

print(check_space(sample_board,5))

#checking if board is full
def is_board_full(board):
   for i in range(1,10):
       if check_space(board,i):
           return False
   return True

print(is_board_full(sample_board))

#placing marker on a specific position that player chooses
def choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board, position):
        position = int(input('Please choose 1 - 9 to place your marker'))
    return position

#if we want to play again
def replays():
    return input('Do you want to play again? Press Y or N').lower()

# THE GAME

print('Welcome to my first game --- TIC TAC TOE')

while True:
    #create new board
    the_board = [' ']*10
    player1_mark, player2_mark = player_input()
    turn = plays_first()
    print('The first one to play is: ' + turn)
    #ask the player to play the game
    play_the_game = input('Would you like to play this lovely game? Press Y or N')
    #if the player is up for a game, game starts, if not they do not play
    if play_the_game.lower() == 'y':
        game_is_on = True
    else:
        game_is_on = False

    #lets play the game

    while game_is_on:
        # Player 1 plays
        if turn == 'Player 1':
            board_display(the_board)
            move = choice(the_board)
            place_the_marker(the_board, move, player1_mark)
            #check for win
            if check_for_win(the_board,player1_mark):
                board_display(the_board)
                print('Well done, you won the game')
                game_is_on = False
            #check for draw
            else:
                if is_board_full(the_board):
                    board_display(the_board)
                    print(('The game is draw this time'))
                    break
                else:
                    turn = 'Player 2'
        else:
            #It is player 2 turn
            board_display(the_board)
            move = choice(the_board)
            place_the_marker(the_board, move, player2_mark)
                #check for win
            if check_for_win(the_board, player2_mark):
                board_display(the_board)
                print('Well done player 2, you won the game')
                game_is_on = False
                #check for draw
            else:
                if is_board_full(the_board):
                    board_display(the_board)
                    print('The game is a draw, please try again')
                    break
                else:
                    turn = 'Player 1'
    #if you want to replay the game
    if not replays():
        break
