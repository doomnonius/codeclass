def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
assert fac(0) == 1
assert fac(5) == 120

def power(b,p):
    """Returns b**p.
    """
    result = 1
    for i in range(0, p):
        result *= b
    return result

print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))

def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # or result += e
    return result

# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42

def summedOdds(L):
    """Loop-based function to return a number.
       Argument: L, a list of integers.
       Result: the sum of all the odd elements in L.
    """
    result = 0
    for i in L:
        if i % 2 == 1:
            result += i
    return result

# tests!
assert summedOdds([4, 5, 6]) == 5
assert summedOdds(range(3, 10)) == 24

def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])  # recursion is OK in this function!

import random

def countGuesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # we just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # guess again!
        numguesses += 1                      # add one to our number of guesses
    return numguesses

def untilARepeat(high):
    """Randomly guess numbers from 0 to high until a number is guessed that has already been guessed.
    """
    L = []
    guess = random.choice(range(0, high))
    L.append(guess)
    numguesses = 1
    while unique(L):
        guess = random.choice(range(0, high))
        L.append(guess)
        numguesses += 1
    return numguesses

print(untilARepeat(10000))
    
def double_char(str):
  x = ''
  for i in range(len(str)):
    x += str[i]
    x += str[i]
  return x

print(double_char("Hello"))

def count_hi(str):
  result = 0
  for i in range(len(str)):
    if str[i:i+2] == 'hi':
      result += 1
  return result

print(count_hi("hihihi"))

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      cat += 1
  for i in range(len(str)):
    if str[i:i+3] == 'dog':
      dog += 1
  if dog == cat:
    return True
  else:
    return False

print(cat_dog("catdog"))

def count_code(str):
  sum = 0
  for i in range(len(str)):
    if (i + 3) <= len(str): 
      if str[i:i+2] == "co" and str[i+3] == "e":
        sum += 1
  return sum

print(count_code("cozexxcope"))

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a) > len(b):
    if a[-(len(b))::1] == b:
      return True
  elif len(b) > len(a):
    print(b[-(len(a))::1])
    print(a)
    if b[-(len(a))::1] == a:
      return True
  else:
    if a == b:
      return True


print(end_other('AbC', 'HiaBc'))