import random
from copy import deepcopy
answer = '2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19'
answer = answer.split()
answer = [int(x) for x in answer]
# arr = list(range(1, 50001))
arr = answer
# random.shuffle(arr)

def minimumSwaps(arr):
    # count how many items are out of place
    arr = [x-1 for x in arr]
    new = deepcopy(arr)
    d = {x:i for i,x in enumerate(arr)}
    print(d)
    count = 0
    for i,x in enumerate(arr):
        # print("i: " + str(i) + ", x: " + str(x))
        if i != new[i]: # because we're moving left to right
            count += 1
            new[d[i]] = new[i] # put original value in place where proper value was
            # reassign so there are no snafus in our index search
            new[i] = i
            d[new[i]] = d[i] # new location
            d[i] = i # because i is now at i
            # print(new)
            # print(d)
    print(d)
    return count, new

print(minimumSwaps(arr))