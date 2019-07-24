
def cost(n):
    if n == 0:
        return 1
    else:
        print (n)
        return cost(n-1) + cost(n-1) # touches all elements of n 
        
print(cost(4))
# print(cost(2))
# print(cost(3))
# print(cost(4))