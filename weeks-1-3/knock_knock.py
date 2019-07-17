# knock_knock.py
def who(x):
    """
    Check if input from user == who's there
    """
    whos_there = input('Knock. Knock. ')
    # base case
    if whos_there == "Who's there?" and x != 0:
        banana_who = input('Banana. ')
        if banana_who == "Banana who?":
            who(x-1)
            #return("Banana")
        else:
            print("Wrong, try again.")
            who(3)
    elif x == 0:
        orange_who = input('Orange. ')
        if orange_who == "Orange who?":
            print("Orange you glad I didn't say banana?")

    else:
        print("Wrong, try again.")
        who(3)
    # recursive

who(3)