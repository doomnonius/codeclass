def powerSet(arr):
    L = [[]]
    while len(arr) >= 0:
        if arr == []:
            return L
        for x in range(len(L)):
            L.append(L[x] + [arr[0]])
        arr = arr[1:]

print(powerSet([1,2]))