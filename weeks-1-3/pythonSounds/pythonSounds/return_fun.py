from random import *

def returnFun():
    return lambda x: x * choice([1, 2, 3, 4, 5, 6, 7])


f = returnFun()
print(f(4))
