# Devon Doornbos
# June 21, 2019, 15:40

# leng example from class
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng(s[1:])

def abs (n):
	'''Returns the absolute value of n'''
	if n < 0:
		n = n - n - n
		return n
	else:
		return n

def neg (n):
	'''Returns the negative of a number'''
	if n > 0:
		n = n - n - n
		return n
	else:
		return n

def mult (n, m):
	'''Returns the product of n and m, but without using multiplication!'''
	#base case
	if m == 0 or n == 0:
		return 0
	elif m < 0 and n > 0:
		return (neg(n) + mult (n, m+1))
	elif m < 0 and n < 0:
		return (abs(n) + mult (n, m+1))
	else:
		return (n + mult (n, m-1))

#
# Tests
#
assert mult(6, 7)   ==  42
assert mult(6, -7)  == -42
assert mult(-6, 7)  == -42
assert mult(-6, -7) ==  42
assert mult(6, 0)   ==   0
assert mult(0, 7)   ==   0
assert mult(0, 0)   ==   0

def dot (L, K):
	'''Finds the dot product of two lists of equal length'''
	#base case
	if len (L) == 0 or len(K) == 0:
		return 0.0
	elif len(L) != len(K):
		return 0.0
	else:
		return L[0] * K[0] + dot (L[1:], K[1:])

#
# Tests
#
assert dot([5, 3], [6, 4])                       == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6])                          == 0.0
assert dot([], [6])                              == 0.0
assert dot([], [])                               == 0.0


def ind (e, L):
	'''Returns the index at which e is first found in L'''
	#base case: if e is not in L
	if len(L) == 0:
		return 0
	elif e == L[0]:
		return 0
	else:
		return 1 + ind(e, L[1:])

#
# Tests
#
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100)))       == 42
assert ind('hi', ['hello', 42, True])     == 3
assert ind('hi', ['well', 'hi', 'there']) == 1
assert ind('i', 'team')                   == 4
assert ind(' ', 'outer exploration')      == 5

def letterScore(let):
	'''Takes a single character string and returns its value as a Scrabble tile.'''
	if let in 'aeilnorstu':
		return 1
	elif let in 'dg':
		return 2
	elif let in 'bcmp':
		return 3
	elif let in 'fhvwy':
		return 4
	elif let in 'k':
		return 5
	elif let in 'jx':
		return 8
	elif let in 'qz':
		return 10
	else:
		return 0

assert letterScore('a') == 1
assert letterScore('d') == 2
assert letterScore('m') == 3
assert letterScore('v') == 4
assert letterScore('k') == 5
assert letterScore('j') == 8
assert letterScore('z') == 10

def scrabbleScore(S):
	'''Takes a string with only lowercase characters and return the Scrabble score of that string.'''
	if len(S) == 0:
		return 0
	else:
		return letterScore(S[0]) + scrabbleScore(S[1:])

#
# Tests
#
assert scrabbleScore('quetzal')                    == 25
assert scrabbleScore('jonquil')                    == 23
assert scrabbleScore('syzygy')                     == 25
assert scrabbleScore('abcdefghijklmnopqrstuvwxyz') == 87
assert scrabbleScore('?!@#$%^&*()')                == 0
assert scrabbleScore('')                           == 0

def transcribe (S):
	'''DNA -> RNA transcription. Create the molecules of mRNA that match a DNA string S.'''
	if len(S) == 0:
		return ''
	elif S[0] in 'ACGT':
		if S[0] == 'A':
			return 'U' + transcribe(S[1:])
		elif S[0] == 'C':
			return 'G' + transcribe(S[1:])
		elif S[0] == 'G':
			return 'C' + transcribe(S[1:])
		else:
			return 'A' + transcribe(S[1:])
	else:
		return '' + transcribe(S[1:])

#
# Tests
#
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU' # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that the other characters disappear
assert transcribe('')         == ''
