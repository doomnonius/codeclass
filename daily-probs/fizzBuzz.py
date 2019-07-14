for x in range(1, 101):
    if x % 3 == 0:
        print('fizz', end='')
    if x % 5 == 0:
        print('buzz', end='')
    if x % 5 != 0 and x % 3 != 0:
        print(x, end='')
    print('')