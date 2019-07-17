def filter(pred, L):
    """ Accepts a predicate (pred) and a list (l).
        Returns a new list containing only the items from li
        where pred(l) matches (returns true).
    """
    #base case: empty list
    if L == []:
        return []
    elif pred(L[0]):
        return [L[0]] + filter(pred, L[1:])
    else:
        return [] + filter(pred, L[1:])

assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
assert filter(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == [1, 2, 4, 5]



def map(func, L):
    """ Accepts a function (func) and a list (l).
        Returns a new list that is the result of applying func
        to every element of l.
    """
    #base case: empty list
    if L == []:
        return []
    else:
        return [func(L[0])] + map(func, L[1:])

assert map(lambda x: x * 2, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
assert map(len, ['hello', 'bob']) == [5, 3]


def reduce(func, L, init):
    """ Accepts a function of two arguments (func), a list (L) and an
        initial value. Applies func cumulatively to the items of l 
        from left to right, starting with the value in init, 
        so as to reduce the list to a single value.
    """
    #base case
    if L == []:
        return init
    else:
        return reduce(func, L[1:], func(init, L[0]))


assert reduce(lambda x, y: x + y , [1, 2, 3, 4, 5], 0) == 15
assert reduce(lambda x, y: x * y , [1, 2, 3, 4, 5], 1) == 120
assert reduce(lambda x, y: x + ' ' + y , ['hello', 'bob'], '') == ' hello bob'


def count(pred, L):
    """ Accepts a predicate (pred) and a list (l).
    Returns the number of items in l where pred(l) matches (returns true).
    """
    #using recursion
    #base case: empty string
    if L == []:
        return 0
    elif pred(L[0]):
        return 1 + count(pred, L[1:])
    else:
        return 0 + count(pred, L[1:])

def count(pred, L):
    """ Accepts a predicate (pred) and a list (l).
    Returns the number of items in l where pred(l) matches (returns true).
    """
    #using filter
    return len(filter(pred, L))

def falseTruth(pred, L):
    '''Accepts L and returns 1 if for items of L that are true
    and 0 for items that are false'''
    if L == []:
        return []
    elif pred(L[0]):
        return [1] + falseTruth(pred, L[1:])
    else:
        return [0] + falseTruth(pred, L[1:])

def falseTruth2(pred, L):
    def oneOrZero(i):
        if pred(i):
            1
        else:
            0
    oneOrZero = lambda i: 1 if pred(i) else 0
    return map(oneOrZero, L)

def count(pred, L):
    """ Accepts a predicate (pred) and a list (l).
    Returns the number of items in l where pred(l) matches (returns true).
    """
    #using return and map. I don't know why this works.
    #why couldn't I figure out how to do this with just map?
    print(reduce(lambda x, y: x + y , falseTruth(pred, L), 0))
    return reduce(lambda x, y: x + y , map(lambda x: 1 if pred(x) else 0, L), 0)

def count(pred, L):
    """ Accepts a predicate (pred) and a list (l).
    Returns the number of items in l where pred(l) matches (returns true).
    """
    #using list comprehension
    return len([x for x in L if pred(L[x-1])])



assert count(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == 2
assert count(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == 4

'''Design and write a function named blsort(L), 
which will accept a list L and should return a list with the 
same elements as L, but in ascending order. (Note: the second 
character is an "ell" for "list", not a 1 or an "i"!) blsort 
*ONLY NEEDS TO HANDLE LISTS OF BINARY DIGITS*, that is, this 
function can and should assume that L will always be a list 
containing only 0s and 1s. Eg:

blsort([1, 0, 1]) == [0, 1, 1]
blsort([0, 1, 1, 0, 1, 0]) == [0, 0, 0, 1, 1, 1]

You may not call Python's built-in sort function to solve this 
problem! Also, you should not use your own sort (asked in a 
question below), but you may use any other technique to 
implement blsort. In particular, you might want to think 
about how to take advantage of the constraint that the argument
will be a binary list—this is a considerable restriction! 
(Hint: the count function you just wrote could come in handy.)
Remember to document and test your function.'''

def blsort(L):
    def create(x, n):
        #base case: x == 0
        if x == 0:
            return []
        else:
            return [n] + create(x-1, n)
    
    return create(count(lambda x: x == 0, L), 0) + create(count(lambda x: x == 1, L), 1)

mylist = [1, 0, 1, 0, 1, 0, 1, 0]

print(blsort(mylist))

def sortList(L):
    '''Sorts a list by breaking it down into parts, then using merge() to put them back together.'''
    def merge(L1, L2):
        if L1 == []:
            return L2
        elif L2 == []:
            return L1
        elif L1[0] <= L2[0]:
            return [L1[0]] + (merge(L1[1:], L2))
        else:
            return [L2[0]] + (merge(L1, L2[1:]))

    #base case: List has one element
    if len(L) == 1:
        return L
    else:  #code wise this is more simplistic, but memory usage wise it is more complex b/c goes through list twice
        return merge(sortList(L[0::2]), sortList(L[1::2]))

mylist2 = [1234, 34, 2, 3, 4, 1, 7, 3, 5, 10, 10000, 4, 9]
print(sortList(mylist2))