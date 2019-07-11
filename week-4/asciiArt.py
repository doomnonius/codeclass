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

# printRect(4, 6, '%')
        
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

# printTriangle(10, '@', False)
# printTriangle(10, '@', True)

def printBumps(num, s1, s2):
    """Uses print triangle to print the specified num of two symbol "bumps", where each bump is larger than the last
    """
    x = 1
    while x <= num:
        printTriangle(x, s1, True)
        printTriangle(x, s2, False)
        x += 1

# printBumps(4, '%', '#')

def printDiamond(w, s):
    """Prints a diamond of symbol s with max width of w.
    """
    h = w*2 - 1
    r = 1
    c = 1
    space = w - 1
    count = 1
    while r <= w:
        while c <= count:
            print(' ' * space + s, end='')
            if c > 1:
                for x in range(1, c):
                    print(' ' + s, end='')
            c += 1
        count += 1
        print('')
        space -= 1
        r += 1
    space = 0
    c = w - 1
    count = c - 1
    while r > w and r <= h:
        space += 1
        while c > count:
            print(' ' * space + s, end='')
            if c > 1:
                for x in range(1, c):
                    print(' ' + s, end='')
            c -= 1
        count -= 1
        print('')
        r += 1


# printDiamond(4, '&')

def printStripedDiamond(w, s1, s2):
    """Prints a striped diamond of symbols s1 & s2 with max width of w.
    """
    h = w*2 - 1
    r = 1
    c = 1
    space = w - 1
    count = 1
    while r <= w:
        while c <= count:
            print(' ' * space + s1, end='')
            if c > 1:
                for x in range(1, c):
                    if x % 2 == 1:
                        print(' ' + s2, end='')
                    else:
                        print(' ' + s1, end='')
            c += 1
        count += 1
        print('')
        space -= 1
        r += 1
    space = 0
    c = w - 1
    count = c - 1
    while r > w and r <= h:
        space += 1
        while c > count:
            if w % 2 == 1:
                if c % 2 == 0:
                    print(' ' * space + s2, end='')
                    if c > 1:
                        for x in range(1, c):
                            if x % 2 == 1:
                                print(' ' + s1, end='')
                            else:
                                print(' ' + s2, end='')
                else:
                    print(' ' * space + s1, end='')
                    if c > 1:
                        for x in range(1, c):
                            if x % 2 == 1:
                                print(' ' + s2, end='')
                            else:
                                print(' ' + s1, end='')
            else:
                if c % 2 == 1:
                    print(' ' * space + s2, end='')
                    if c > 1:
                        for x in range(1, c):
                            if x % 2 == 1:
                                print(' ' + s1, end='')
                            else:
                                print(' ' + s2, end='')
                else:
                    print(' ' * space + s1, end='')
                    if c > 1:
                        for x in range(1, c):
                            if x % 2 == 1:
                                print(' ' + s2, end='')
                            else:
                                print(' ' + s1, end='')
            c -= 1
        count -= 1
        print('')
        r += 1

printStripedDiamond(15, '.', '%')