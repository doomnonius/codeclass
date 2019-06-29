#
# Lights out in 1D
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.
import sys            # larger recursive stack
sys.setrecursionlimit(10000) # 10000 stack frames availble


def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element

def timesTwo(i, oldL):
    ''' Accepts index i and old list oldL, returns ith element of a new list.'''
    new_i = 2 * oldL[i]
    return new_i

def square(i, oldL):
    '''Accepts index and list, returns i element.'''
    new_i = oldL[i] * oldL[i]
    return new_i

def rot(i, oldL):
    '''Accepts a list and rotates it.'''
    return oldL[i-1]

def rand(i, oldL):
    '''Accepts a list and turns its elements randomly into 0 or 1'''
    new_i = choice([0, 1])
    return new_i

def allOnes(L):
    '''Return true if each element of a list is one'''
    if L == []:
        return True
    elif L[0] == 1:
        return allOnes(L[1:])
    else:
        return False

def toggle(i, oldL, target = 0):
    """ Accepts an index (i), an old list (oldL) and the index to turn on (target).
        turn_on_one returns the ith element of a NEW list!
        * Note that turn_on_one returns ONLY the ith element
          turn_on_one thus needs to be called many times in evolve.
    """
    if i == 0:
        if i == target or i + 1 == target:
            if oldL[i] == 1:
                return 0
            else:
                return 1
        else:
            return oldL[i]
    elif i == len(oldL)-1:
        if i == target or i - 1 == target:
            if oldL[i] == 1:
                return 0
            else:
                return 1
        else:
            return oldL[i]
    else:
        if i == target or (i + 1) == target or (i - 1) == target:
            if oldL[i] == 1:
                return 0
            else:
                return 1      # this makes the game easy!
        else:
            return oldL[i] # the new is the same as the old

def randBL(n):
    '''Returns a random binary list of length n'''
    if n == 0:
        return []
    else:
        return [choice([0,1])] + randBL(n-1)

def vizL(i, oldL):
    '''Returns the index of i'''
    return i

def evolve(oldL, mutate, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    # print(oldL),                    # print the old list, L
    # time.sleep(0.05)
    visual = [vizL(i, oldL) for i in range(len(oldL))]
    print(visual)
    print(oldL)

    if allOnes(oldL):  # we're done!
        print("It took you " + str(curgen) + " generations to solve the puzzle!")      # no return value... yet
    else:
        # user = int(input("Index? "))
        print(range(len(oldL)))
        user = choice(range(len(oldL)))
        print("  (gen: " + str(curgen) + ")")  # and its gen.
        newL = [ mutate(i,oldL,user) for i in range(len(oldL))]
        return evolve(newL, mutate, curgen + 1)

evolve(randBL(10), toggle)