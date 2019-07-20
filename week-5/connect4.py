import random
import time

def listOfWords (S):
	""" Builds from the back of the list. Either adds a new item
	to the list, or adds a character to the string at the head
	of the list
	"""
	#base case
	if len(S) == 0:
		return ['']
	else: 
		c = S[0]
		L = listOfWords(S[1:])
		if S[0] == ' ':
			return [''] + L
		else:
			return [c + L[0]] + L[1:]

def removeUseless(S):
  """Removes commas from a string.
  """
  if len(S) == 0:
    return ''
  if str(S[0]) in '1234567890':
    return str(S[0]) + removeUseless(S[1:])
  elif S[0] == ' ':
      return ' ' + removeUseless(S[1:])
  else:
    return '' + removeUseless(S[1:])

def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

class Board:
    """ A data type representing a Connect-4 board with an arbitrary number of rows and columns.
    """
    def __init__(self, h = 6, w = 7, n = 4):
        """ Constructs objects of type Board, w/ given height and width
        """
        self.height = h
        self.width = w
        self.data = [[' ']* w for row in range(self.height)]
        self.needed_to_win = n

    def __repr__(self):
        """ Returns a string representation for an object of type Board.
        """
        s = ''
        for row in range(0, self.height):
            if self.height <= 10:
                num = abs(row % 10 - self.height + 1)
            else:
                num = abs(row % 10 - 10 + 1)
            s += (str(num) + ' ')
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '  ' + (2*self.width + 1) * '-' + '\n   ' #bottom of board
        for col in range(0, self.width):
            num = col % 10
            s += (str(num) + ' ')
        return s

    def clear(self):
        """ Clears the board.
        """
        self.data = [[' ']* self.width for row in range(self.height)]

    def isFull(self):
        """ Returns True if calling object is full, otherwise False.
        """
        for col in range (0, self.width):
            for row in range(0, self.height):
                if self.data[row][col] == ' ':
                    return False
        return True

    def winsFor(self, ox):
        """ Returns True if four checkers of type ox in a row, False otherwise.
        """
        # My Code
        # #check horizontal
        # for x in range(0, self.height):
        #     for col in range(0, self.width):
        #         opp = abs(x - (self.height - 1))
        #         if self.data[opp][col] == ox and col < (self.width - 3):
        #             if self.data[opp][col + 1] == ox and self.data[opp][col + 2] == ox and self.data[opp][col + 3] == ox:
        #                 return True
        
        # #check vertical
        #         if self.data[opp][col] == ox and opp > 2:
        #             if self.data[opp - 1][col] == ox and self.data[opp - 2][col] == ox and self.data[opp - 3][col] == ox:
        #                 return True

        # #check up-right diagonal
        #         if self.data[opp][col] == ox and opp > 2 and col < (self.width - 3):
        #             if self.data[opp - 1][col + 1] == ox and self.data[opp - 2][col + 2] == ox and self.data[opp - 3][col + 3] == ox:
        #                 return True
        
        # #check up-left diagonal
        #         if self.data[opp][col] == ox and opp > 2 and col > 2:
        #             if self.data[opp - 1][col - 1] == ox and self.data[opp - 2][col - 2] == ox and self.data[opp - 3][col - 3] == ox:
        #                 return True
        # return False

        #Matt's code: (also the functions it calls are his)
        for row in range(self.height):
            for col in range(self.width):
                if inarow_Neast(ox, row, col, self.data, self.needed_to_win) or \
                inarow_Nsouth(ox, row, col, self.data, self.needed_to_win) or \
                inarow_Nnortheast(ox, row, col, self.data, self.needed_to_win) or \
                inarow_Nsoutheast(ox, row, col, self.data, self.needed_to_win):
                    return True
            

class Connect4Board(Board):
    """Includes the rules specifically for the connect board.
    """

    def addMove(self, col, ox):
        """ Takes two arguments, first is the column in which to add the new checker and the second is a one character string representing the checker.
        """
        for x in range(0, self.height):
            opp = abs(x - (self.height - 1))
            if self.data[opp][int(col)] == ' ':
                self.data[opp][int(col)] = ox
                break

    def allowsMove(self, c):
        """ Returns True if a move is allowed into column c. Returns False if a column is full or not a legal number to call
        """
        if int(c) > (self.width - 1) or int(c) < 0:
            return False
        else:
            if self.data[0][int(c)] != ' ':
                return False
            else:
                return True

    def delMove(self, c):
        """ Removes the top checker of column c, does nothing if column is empty.
        """
        for x in range(0, self.height):
            if self.data[x][c] != ' ':
                self.data[x][c]= ' '
                break

    def colsToWin(self, ox):
        """ Checks to see if any placements would provide a win for player ox.
        """
        self.wins = []
        for col in range(0, self.width):
            if self.allowsMove(col):
                self.addMove(col, ox)
                if self.winsFor(ox):
                    self.wins += [col]
                self.delMove(col)
        return self.wins

    def setBoard(self, move):
        """ Accepts a string of columns and places, alternating checkers in those columns, starting with 'X'.
            Input must be a string of one digit integers.
        """
        nextChecker = 'X'
        for colChar in move:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def aiMove(self, ox):
        """ Chooses which move the AI will make.
        """
        self.winsX = self.colsToWin('X')
        self.winsO = self.colsToWin('O')
        if ox == 'X' and self.winsX != []:
            self.addMove(random.choice(self.winsX), ox)
        elif ox == 'X' and self.winsX == [] and self.winsO != []:
            self.addMove(random.choice(self.winsO), ox)
        elif ox == 'X' and self.winsX == [] and self.winsO == []:
            allowed = []
            for i in range(0, self.width):
                if self.allowsMove(i):
                    allowed += [i]
            self.addMove(random.choice(allowed), ox)
        if ox == 'O' and self.winsO != []:
            self.addMove(random.choice(self.winsO), ox)
        elif ox == 'O' and self.winsO == [] and self.winsX != []:
            self.addMove(random.choice(self.winsX), ox)
        elif ox == 'O' and self.winsX == [] and self.winsO == []:
            allowed = []
            for i in range(0, self.width):
                if self.allowsMove(i):
                    allowed += [i]
            self.addMove(random.choice(allowed), ox)


    def hostGame(self):
        """ Brings it all together into the familiar game.
        """
        ai = int(input("How many ai will be playing? "))
        if ai == 1:
            ai2 = input("Will the ai play as X or O? ")
        else:
            ai2 = 'X'
        while True:
            player = "X"
            print(self)
            print("X's turn!")
            if ai > 0 and ai2 == 'X':
                self.aiMove(player)
                if ai == 2:
                    ai2 = 'O'
            else:
                col = input("Enter which column to drop your piece into: ")
                while not self.allowsMove(col):
                    print("That's not a valid move! Try again, X!")
                    col = input("Enter which column to drop your piece into: ")
                self.addMove(col, player)
            if self.winsFor(player):
                print(self)
                print("X wins!")
                break
            if self.isFull():
                print(self)
                print("Draw!")
                break
            player = "O"
            print(self)
            print("O's turn!")
            if ai > 0 and ai2 == 'O':
                self.aiMove(player)
                if ai == 2:
                    ai2 = 'X'
            else:
                col = input("Enter which column to drop your piece into: ")
                while not self.allowsMove(col):
                    print("That's not a valid move! Try again, O!")
                    col = input("Enter which column to drop your piece into: ")
                self.addMove(col, player)
            if self.winsFor(player):
                print(self)
                print("O wins!")
                break
            if self.isFull():
                print(self)
                print("Draw!")
                break

class GridBoard(Board):
    def allowsMove(self, row, col):
        if row > self.height - 1:
            return False
        if col > self.width - 1:
            return False
        if self.data[row][col] != ' ':
            return False
        return True
    
    def addMove(self, row, col, ox):
        """ Modifies this board by placing the given character/piece
            in the space at the given row and column.
        """
        self.data[row][col] = ox

    def delMove(self, row, col):
        """ Modifies this board by removing the character/piece
            in the given row and column
        """
        self.data[row][col] = ' '

    def playerTurn(self, ox):
        """ The actions of a player's turn.
        """
        userInput = input("Enter which row and column to drop your piece into: ")
        if userInput == '':
            KeyError
        inputs = listOfWords(removeUseless(userInput))
        while len(inputs) != 2:
            print("Enter exactly two numbers, please!")
            userInput = input("Enter which row and column to drop your piece into: ")
            inputs = listOfWords(removeUseless(userInput))
        while len(inputs) > 0:
            try:
                row = int(inputs[0])
                col = int(inputs[1])
                break
            except:
                print("Enter only numbers, please!")
                userInput = input("Enter which row and column to drop your piece into: ")
                inputs = listOfWords(removeUseless(userInput))  
        while not self.allowsMove((self.height - int(inputs[0]) - 1), col):
            print("That's not a valid move! Try again, X!")
            userInput = input("Enter which column to drop your piece into: ")
            inputs = listOfWords(removeUseless(userInput))
            while len(inputs) != 2:
                print("Enter exactly two numbers, please!")
                userInput = input("Enter which row and column to drop your piece into: ")
                inputs = listOfWords(removeUseless(userInput))
            while len(inputs) > 0:
                try:
                    row = int(inputs[0])
                    col = int(inputs[1])
                    break
                except:
                    print("Enter only numbers, please!")
                    userInput = input("Enter which row and column to drop your piece into: ")
                    inputs = listOfWords(removeUseless(userInput))  
        row = self.height - int(inputs[0]) - 1
        self.addMove(row, col, ox)

class TicTacToeBoard(GridBoard):

    def hostGame(self):
        """ Brings it all together into the familiar game.
        """
        while True:
            player = "X"
            print(self)
            print("X's turn!")
            self.playerTurn(player)
            if self.winsFor(player):
                print(self)
                print("X wins!")
                break
            if self.isFull():
                print(self)
                print("Draw!")
                break
            player = "O"
            print(self)
            print("O's turn!")
            self.playerTurn(player)
            if self.winsFor(player):
                print(self)
                print("O wins!")
                break
            if self.isFull():
                print(self)
                print("Draw!")
                break

class PenteBoard(GridBoard):
    def hostGame(self):
        """ Brings it all together into the familiar game.
        """
        while True:
            try:
                players = int(input("How many players will be playing [2, 3, or 4]?"))
                if players > 4 or players < 2:
                    assert 1 < players < 5
                break
            except:
                print("Enter a number from 2-4.")
                players = int(input("How many players will be playing [2, 3, or 4]?"))
        while True:
            player = "X"
            print(self)
            print("X's turn!")
            self.playerTurn(player)
            if self.winsFor(player):
                print(self)
                print("X wins!")
                break
            if self.isFull():
                print(self)
                print("Draw!")
                break
            player = "O"
            print(self)
            print("O's turn!")
            self.playerTurn(player)
            if self.winsFor(player):
                print(self)
                print("O wins!")
                break
            if self.isFull():
                print(self)
                print("Draw!")
                break
            if players > 2:
                player = "V"
                print(self)
                print("V's turn!")
                self.playerTurn(player)
                if self.winsFor(player):
                    print(self)
                    print("V wins!")
                    break
                if self.isFull():
                    print(self)
                    print("Draw!")
                    break
                if players == 4:
                    player = "A"
                    print(self)
                    print("A's turn!")
                    self.playerTurn(player)
                    if self.winsFor(player):
                        print(self)
                        print("A wins!")
                        break
                    if self.isFull():
                        print(self)
                        print("Draw!")
                        break