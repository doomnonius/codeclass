import random
""" You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N qheens can be placed on the board without threatening each other.
"""
# Initial ideas: create a recursive function?

def addQueen(board):
    """ Adds another queen to the board. Returns
    """
    # base case
    out = 0
    for x in board:
        for y in x:
            if y == ' ':
                out += 1
    if out == 0:
        return 1
    rand1 = random.choice(range(len(board)))
    rand2 = random.choice(range(len(board)))
    while board[rand1][rand2] != ' ':
        rand1 = random.choice(range(len(board)))
        rand2 = random.choice(range(len(board)))
    board[rand1][rand2] = 'q'
    board = disallow(rand1, rand2, board)


    
    return out * addQueen(board)
    

def disallow(x, y, board):
    """ Changes the board.
    """
    count = 0
    oy = y
    ox = x
    while count < len(board):
        y += 1
        board[x][y % len(board)] = 'd'
        count += 1
    count = 0
    while count < len(board):
        x += 1
        board[x % len(board)][oy] = 'd'
        count += 1
    count = 0
    while count < len(board):
        x += 1
        y += 1
        board[ox % len(board)][oy % len(board)] = 'd'
        count += 1
    return board

def makeBoard(N):
    """ Creates a board of N by N size.
    """
    board = [[' '] * N] * N
    return board

print(addQueen(makeBoard(8)))