import random
from copy import deepcopy

def createOneRow(w):
    """Returns one row of zeros of width w.
       For use in the createBoard function.
    """
    row = []
    for col in range(w):
        row += [0]
    return row

def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for rows in A:               # row is the whole row
        for cols in rows:         # col is the individual element
            print(cols, end='')
        print('')  # print that element
    print('')

def createBoard(w, h):
    """ Returns a 2D array with h rows and w columns.
    """
    columns = []
    for x in range(h):
        columns += [createOneRow(w)]
    return columns

def diagonalize(w, h):
    """ Creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
        But do that only in the *interior* of the 2D array.
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(w, h):
    """Turns on all cells except the outside row.
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1

    return A

def randomCells(w, h):
    """Turns on interior cells at random.
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0, 1])

    return A

def copy(A):
    """ Deep copies our 2D array.
    """
    h = len(A)
    w = len(A[0])
    newA = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            newA[row][col] = A[row][col]

    return newA

def innerReverse(A):
    h = len(A)
    w = len(A[0])
    newA = deepcopy(A)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    
    return newA

def countNeighbors(row, col, A):
    """ Returns the number of live neighbors for a cell in board A at a      particular row and col. Uses modulo to wrap around the edges.
    """
    acc = 0
    # the row below
    if A[(row + 1)%len(A)][(col - 1)%len(A[0])] == 1:
        acc += 1
    if A[(row + 1)%len(A)][col] == 1:
        acc += 1
    if A[(row + 1)%len(A)][(col + 1)%len(A[0])] == 1:
        acc += 1
    # the row
    if A[row][(col - 1)%len(A[0])] == 1:
        acc += 1
    if A[row][(col + 1)%len(A[0])] == 1:
        acc += 1
    # the row above
    if A[(row - 1)%len(A)][(col - 1)%len(A[0])] == 1:
        acc += 1
    if A[(row - 1)%len(A)][col] == 1:
        acc += 1
    if A[(row - 1)%len(A)][(col + 1)%len(A[0])] == 1:
        acc += 1
    return acc

def checkEdge(row, col, A):
    if row == 0:
        return True
    if row == (len(A)) - 1:
        return True
    if col == 0:
        return True
    if col == (len(A[0]) - 1):
        return True
    return False

def next_life_generation(A):
    """ Makes a copy of A and then advances one
        generation of Conway's Game of Life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """
    h = len(A)
    w = len(A[0])
    newA = deepcopy(A)
    
    for row in range(0, h):
        for col in range(0, w):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) == 3 and A[row][col] == 0:
                newA[row][col] = 1
            elif countNeighbors(row, col, A) < 4 and A[row][col] == 1:
                newA[row][col] = 1
            elif countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            else:
                newA[row][col] = A[row][col]
    
    return newA

A = [[1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
]

A2 = next_life_generation(A)

A3 = next_life_generation(A2)

printBoard(A)

printBoard(A2)

printBoard(A3)