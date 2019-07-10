def numberOfDigits(x):
    '''Determines how many integers a positive number has'''
    try:
        x = int(x)
    except:
        print("That's not an integer.")
    # base case
    if x < 10:
        return 1
    else:
        return 1 + numberOfDigits(x/10)

print(numberOfDigits(234325))

def maxInList(L):
    '''Returns the largest number from a list of integers'''
    # base case
    if len(L) == 0:
        return 0
    
    return max(L[0], maxInList(L[1:]))

my_list = [12, 354, 34, 43543, 23, 324, 4, 234, 23]
print(maxInList(my_list))

# def isPalindrome(x):

def eatChocolate(money, price, wrap, wraps = 0):
    '''
    Takes amount of money, price of chocolate, and number of wrappers that
    grants a free chocolate and returns the amount of chocolates that
    will be consumed
    '''
    # base case: money < price
    if money < price:
        if wraps < wrap:
            return 0
        else:
            return 1 + eatChocolate(money, price, wrap, wraps - wrap + 1)
    else:
        # print("Money: ", money)        
        return 1 + eatChocolate(money-price, price, wrap, wraps + 1)


print(eatChocolate(20, 3, 5))
