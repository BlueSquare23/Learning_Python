#!/usr/local/bin/python3
#Johnnyboi wrote this game for the fun of it

print("Tic Tac Toe")
print("--------------------------------")

'''
Its the classic game of Tic Tac Toe!
'''
print("Welcome to the classic game of Tic Tac Toe!")

#Game Rules
print("""
Rules:

Select the cordinates on the game board where you'd like to place your mark.
Player1 is an 'X' and Player2 is an 'O'
The first person to get three in a row wins!

The game board looks like this,

___|___|_X_
___|___|___
   |   |

The 'X' is at the cordinates (1, 3). Where One is the row and Three is the
column.
""")


game = [
[0,0,0],
[0,0,0],
[0,0,0]
]


#Conducts win checking
def win_checker(player):
    #Column check
    #If the column of the 2d array 'game' is all the same value (the players value), return a win status
    if game[0][0] == player and game[1][0] == player and game[2][0] == player:
        print("Left column, player{:d} wins!".format(player))
        exit()
    elif game[0][1] == player and game[1][1] == player and game[2][1] == player:
        print("Middle column, player{:d}wins!".format(player))
        exit()
    elif game[0][2] == player and game[1][2] == player and game[2][2] == player:
        print("right column, player{:d} wins!".format(player))
        exit()
    #Row check
    elif game[0][0] == player and game[0][1] == player and game[0][2] == player:
        print("Top row, player{:d} wins!".format(player))
        exit()
    elif game[1][0] == player and game[1][1] == player and game[1][2] == player:
        print("Middle row, player{:d} wins!".format(player))
        exit()
    elif game[2][0] == player and game[2][1] == player and game[2][2] == player:
        print("Bottom row, player{:d} wins!".format(player))
        exit()
    #Diagonal check
    elif game[0][0] == player and game[1][1] == player and game[2][2] == player:
        print("Diagonal, player{:d} wins!".format(player))
        exit()
    elif game[0][2] == player and game[1][1] == player and game[2][0] == player:
        print("Diagonal, player{:d} wins!".format(player))
        exit()
    else:
        return "null"


#Processes user input
def player_move(player):
    #Tells the player to go
    print("Player{:d} choose your move,".format(player))
    player_row = int(input("Choose your row, ")) - 1
    player_col = int(input("Choose your column, ")) - 1
    #player_mov = [player_row, player_col]
    #return player_mov
    if game[player_row][player_col] != 0:
        print("The other player has already chosen that space!")
        print("Please enter a different set of cordinates, ")
        player_move(player)
    else:
        game[player_row][player_col] = player
        game_board()

#Print board
def game_board():
    #First Row
    a = game[0][0]
    #print(a)
    if a == 0:
        a = '_'
    elif a == 1:
        a = 'X'
    elif a == 2:
        a = 'O'
    b = game[0][1]
    #print(b)
    if b == 0:
        b = '_'
    elif b == 1:
        b = 'X'
    elif b == 2:
        b = 'O'
    c = game[0][2]
    #print(c)
    if c == 0:
        c = '_'
    elif c == 1:
        c = 'X'
    elif c == 2:
        c = 'O'

    #Second Row
    d = game[1][0]
    #print(d)
    if d == 0:
        d = '_'
    elif d == 1:
        d = 'X'
    elif d == 2:
        d = 'O'
    e = game[1][1]
    #print(e)
    if e == 0:
        e = '_'
    elif e == 1:
        e = 'X'
    elif e == 2:
        e = 'O'
    f = game[1][2]
    #print(f)
    if f == 0:
        f = '_'
    elif f == 1:
        f = 'X'
    elif f == 2:
        f = 'O'

    #Third Row
    g = game[2][0]
    #print(g)
    if g == 0:
        g = '_'
    elif g == 1:
        g = 'X'
    elif g == 2:
        g = 'O'
    h = game[2][1]
    #print(h)
    if h == 0:
        h = '_'
    elif h == 1:
        h = 'X'
    elif h == 2:
        h = 'O'
    i = game[2][2]
    #print(i)
    if i == 0:
        i = '_'
    elif i == 1:
        i = 'X'
    elif i == 2:
        i = 'O'

    print('_{:s}_|_{:s}_|_{:s}_'.format(a, b, c))
    print('_{:s}_|_{:s}_|_{:s}_'.format(d, e, f))
    print(' {:s} | {:s} | {:s} '.format(g, h, i))

#Game Loop
def play_game():

    player_move(1)
    if win_checker(1) == 'null':
        player_move(2)
        if win_checker(2) == 'null':
            play_game()
    else:
        print("Game Over!")
        exit()

play_game()
