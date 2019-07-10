def numToBaseX(n, x):
    """Converts a number to any base less than ten.
    """
    if n == 0:
        return ''
    else:
        return numToBaseX((n - (n % x))//x, x) + str(n % x)

def numToTern(n):
    """Converts a number in base 10 to a string in base 2.
    """
    #base case: n == 0
    if n == 0:
        return ''
    else:
        return numToTern((n-(n % 3))//3) + str(n % 3)

def ternToNum(S):
    """Converts a string from base 3 to base 10
    """
    if len(S) == 1:
        return int(S[0])
    else:
        return (ternToNum(S[:-1]) * 3) + int(S[-1])

def baseXToNum(S, x):
    """Converts a string from base X (1 < X < 10) to base 10
    """
    if len(S) == 1:
        return int(S[0])
    else:
        return (baseXToNum(S[:-1], x) * x) + int(S[-1])

# print(baseXToNum(numToBaseX(42, 4), 4))

def numToBTern(n):
    """Converts a number to Balanced Ternary.
    """
    if n == 0:
        return ''
    elif n % 3 == 1:
        return numToBTern((n - (n % 3)) // 3) + '+'
    elif n % 3 == 2:
        return numToBTern((n + (n % 3)) // 3) + '-'
    else:
        return numToBTern(n // 3) + '0'
        

def bTernToNum(S):
    """Converts a string of Balanced Ternary to a number.
    """
    if len(S) == 1:
        if S[0] == '-':
            return -1
        elif S[0] == '+':
            return 1
        else:
            return 0
    else:
        if S[-1] == '-':
            return (bTernToNum(S[0:-1]) * 3) - 1
        elif S[-1] == '+':
            return (bTernToNum(S[0:-1]) * 3) + 1
        else:
            return (bTernToNum(S[0:-1]) * 3)

print(bTernToNum(numToBTern(42)))