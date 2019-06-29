def filter(pred, l):
    """ Accepts a predicate (pred) and a list (l).
        Returns a new list containing only the items from l
        where pred(l) matches (returns true).
    """
    # base case: list is empty
    if l == []:
        return []
    # recursive step: list isn't empty
    else:
        # if predicate is true add it to a list then run again l[:1]
        if pred(l[0]):
            return [l[0]] + filter(pred(l[0]), l[1:])
        # if predicate is false chuck it then run again l[1:]
        else:
            return filter(pred(l[0]), l[1:])

#print(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
#assert filter(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == [1, 2, 4, 5]