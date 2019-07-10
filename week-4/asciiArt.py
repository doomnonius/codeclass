def printRect(w, h, s):
    """Arguments: width, height, symbol. Creates a rectangle using specified symbol to specified dimensions.
    """
    x = w
    while h > 0:
        while w > 0:
            print(s + ' ', end='')
            w -= 1
        print('')
        w = x
        h -= 1

printRect(4, 6, '%')
        
def printTriangle(w, s, right):
    """Arguments: width, symbol, right side up (boolean) and prints a triangle of said dimension and said symbol.
    """
    if right:
        h = w
        y = w
        z = w - 1
        while h > 0:
            while w > z:
                print(s + ' ', end='')
                w -= 1
            print('')
            y += 1
            w = y
            h -= 1
    else:
        x = w  # x is height
        while x > 0:
            while w > 0:
                print(s + ' ', end='')
                w -= 1
            print('')
            x -= 1
            w = x

printTriangle(10, '@', False)
printTriangle(10, '@', True)

def printBumps(num, s1, s2):
    """Uses print triangle to print the specified num of two symbol "bumps", where each bump is larger than the last
    """
    x = 1
    while x <= num:
        printTriangle(x, s1, True)
        printTriangle(x, s2, False)
        x += 1

printBumps(4, '%', '#')
