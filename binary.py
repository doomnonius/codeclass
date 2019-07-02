def oddParity(n):
    """Returns true for odd numbers and false for even numbers.
    """
    if n % 2 == 1:
        return True
    else:
        return False

"""The base 2 representation of 42 is 101010"""
"""An odd binary number will have a 1 on the right, and an even one will have a zero."""
""""Attaching a zero doubles. Attaching a one doubles and adds one."""

def numToBinary(n):
    """Converts a number from base ten to base two.
    """
    #base case: n == 0
    if n == 0:
        return ''
    else:
        return numToBinary((n-(n % 2))//2) + str(n % 2)

print(numToBinary(2342))

def binaryToNum(S, n = 0):
    """Converts a number from base two to base ten."""
    if S == '':
        return 1
    else:
        return binaryToNum(S[0:-1], n + 1) + int(S[-1])*2**n

def binaryToNum(S):
    """Converts a number from base two to base ten, but better."""
    if S == '1':
        return 1
    else:
        return (binaryToNum(S[0:-1]) * 2) + int(S[-1])

def increment(S):
    """Takes an input of 8 bit string of 0s and 1s and returns next largest number in base 2"""
    #base case: empty string
    if S == '':
        return ''
    elif S[-1] == '0':
        S = str(int(S) + 1)
        return S
    else:
        return increment(S[0:-1]) + '0'

def count(S, n):
    #base case: n = 0
    print(S)
    if n == 0:
        return
    else:
        return count(increment(S), n - 1)
    

print(binaryToNum('11111111'))