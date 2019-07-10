'''1:removeAll(e, L) takes in a list L and an element e (really any data whatsoever). Then, removeAll should return another list that is \
 identical to L except that all elements identical to e have been removed. Notice that e has to be a top-level element to be removed, \
  as the examples illustrate:
>>> from hw1pr4 import *
>>> removeAll(42, [ 55, 77, 42, 11, 42, 88 ])
[ 55, 77, 11, 88 ]
>>> removeAll(42, [ 55, [77, 42], [11, 42], 88 ])
[ 55, [77, 42], [11, 42], 88 ]
>>> removeAll([77, 42], [ 55, [77, 42], [11, 42], 88 ])
[ 55, [11, 42], 88 ]
Aside: It's possible to write removeAll so that it works even if the second input is a string instead of a list, \
but you do not need to do this here.'''

def removeAll(e,L):
	if len(L) == 0:
		return []
	elif L[0] == e:
		return [] + removeAll(e,L[1:])
	else:
		return [L[0]] + removeAll(e,L[1:])

'''2:zipper(L, K) takes in two lists L and K and should output a single list of two-element sublists.\
 Each of these two-element sublists should contain corresponding elements of L and K. \
 If one of the two lists, L or K is longer than the other, the extra elements are discarded. For example:
>>> from hw1pr4 import *
>>> zipper([], [1,2,3])
[]
>>> zipper([1,2], ['a','b','c'])
[ [1,'a'], [2,'b'] ]
>>> zipper([42]*3, [ 'tiles in scrabble', 'km in a '\
'marathon' ])
[ [42, 'tiles in scrabble'], [42,'km in a marathon'] ]
Aside: your zipper will probably work as-is with strings, if it works for lists.'''

def zipper (L, K):
	if len(L) == 0 or len(K) == 0:
		return []
	else:
		test = [[L[0], K[0]]]
		#print(test)
		ziptest = zipper(L[1:], K[1:])
		#print(ziptest)
		return test + ziptest

# print(zipper([1, 2], ['a','b','c']))

'''3:ind(e, L) takes in a sequence L and an element e. L might be a string or, more generally, a list. \
Then, ind should return the index at which e is first found in L. Counting begins at 0, as is usual with lists. \
If e is NOT an element of L, then ind(e, L) should return an integer that is at least the length of L. \
It can be len(L) exactly, as the example below returns, or any integer larger than that.
>>> from hw1pr4 import *
>>> ind(42, [ 55, 77, 42, 12, 42, 100 ])
2
>>> ind(42, range(0,100))
42
>>> ind('hi', [ 'hello', 42, True ])
3
>>> ind('hi', [ 'well', 'hi', 'there' ])
1 
>>> ind('i', 'team')
4 
>>> ind(' ', 'outer exploration')
5 '''

def ind(e, L):
	'''Returns the index at which e is first found in L'''
	#base case: if e is not in L
	if len(L) == 0:
		return 0
	elif e == L[0]:
		return 0
	else:
		return 1 + ind(e, L[1:])


'''4:listOfWords(S) takes as input a string S and should return a list of the "words" in S. \
By "words" we mean space-separated substrings of non-space characters. \
None of the "words" should be the empty string or contain a space. \
On the empty string listOfWords('') should return the empty list. Consider these examples:
>>> from hw1pr4 import *'''

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


print(listOfWords('Bond. James Bond'))
#[ 'Bond.', 'James', 'Bond' ]
print(listOfWords(''))
#[]
listOfWords('    ')    # lots of spaces
#[]
listOfWords('  Avada   Ked...   ')  # more spaces
#[ 'Avada', 'Ked...' ]'''