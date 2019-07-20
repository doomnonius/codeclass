"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
import argparse
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument("number", help="print the number of possible interpretations of this number representing a coded message following a=1, ...,  z = 26", type=str)
args = parser.parse_args()

coded = args.number
"""
1 = aaaaa
2 = akaa
3 = aaka
4 = aaak
5 = kaaa
6 = kka
7 = kak
8 = akk
"""
if len(coded) % 2 == 1:
    extra = [0]
else:
    extra = [1]

alpha = [0, "a", "b", "c", "d", "e", 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

counter = []
word = []
words = []

def decode(coded):
    """ Decodes all possibilities of a string encoded as a = 1 ... z = 26
    """
    words = []
    if coded == '':
        return ''
    elif len(coded) == 1:
        words 
    elif int(coded[0:2]) > 26:
        return alpha[int(coded[0])] + decode(coded[1:])
    elif int(coded[0:2]) < 27 and coded[1] != 0:
        words += [alpha[int(coded[0:2])] + coded[2:]]
        words += [alpha[int(coded[0])] + coded[1:]]
    elif int(coded[1]) == 0:
        words += [alpha[int(coded[0:2])] + coded[2:]]
    elif 
    
    
print(reduce(lambda x, y: x*y, counter))

