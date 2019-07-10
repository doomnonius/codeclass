def leng(L):
    if L == []:
        return 0
    else:
        return 1 + leng(L[1:])

print(leng([1, 2, 3]))

def leng(L, acc = 0):
    if L == []:
        return acc
    else:
        return leng(L[1:], acc + 1)

print(leng([1, 2, 3]))

def leng(L):
    acc = 0
    while L != []:
        acc += 1
        L = L[1:]
    return acc

print(leng([1, 2, 3]))