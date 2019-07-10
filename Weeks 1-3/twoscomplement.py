def numToBinary(n):
    """Converts a number from base ten to base two.
    """
    #base case: n == 0
    if n == 0:
        return ''
    else:
        return numToBinary((n-(n % 2))//2) + str(n % 2)

def count(S, n):
    #base case: n = 0
    # print(S)
    if n == 0:
        return S
    else:
        return count(increment(S), n - 1)

def binaryToNum(S):
    """Converts a number from base two to base ten, but better."""
    if S == '':
        return 0
    elif S == '1':
        return 1
    else:
        return (binaryToNum(S[0:-1]) * 2) + int(S[-1])

def flip(S):
    #base case: empty string
    if S == '':
        return ''
    elif S[0] == '1':
        return '0' + flip(S[1:])
    else:
        return '1' + flip(S[1:])

def subtract(S):
    #base case: empty string
    if S == '':
        return ''
    elif S[-1] == '1':
        S = str(int(S) - 1)
        return S
    else:
        return subtract(S[:-1]) + '1'

def increment(S):
    """Takes an input of 8 bit string of 0s and 1s and returns next largest number in base 2 as a string"""
    #base case: empty string
    if S == '':
        return ''
    elif S[-1] == '0':
        S = S[:-1] + str(int(S[-1]) + 1)
        return S
    else:
        return increment(S[0:-1]) + '0'

def TcToNum(S):
    """Takes a string of 8 bits which represents a number in two's complement and returns the number."""
    if S[0] == "1":
        return (binaryToNum(flip(subtract(S))) * -1) 
    else:
        return binaryToNum(S)

def NumToTc(n):
    """Takes a number and returns the two's complement string of eight bits."""
    if n > 255 or n < -128:
        print("Error!")
    elif n >= 0:
        return count('00000000', n)
    else:
        return increment(flip(count('00000000', abs(n))))


print(NumToTc(TcToNum('00000001')))
print(NumToTc(TcToNum('11111111')))
print(NumToTc(TcToNum('10000000')))
print(NumToTc(-200))