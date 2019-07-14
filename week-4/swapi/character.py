import argparse
import csv
import json
import time

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("-s", "--sorting", help="print character.csv sorted by height or weight", type=str, default=False)
group.add_argument('-t', '--tallest', help="find the tallest character in the given movie", type=int)
group.add_argument('-l', '--shortest', help="find the shortest character in the given movie", type=int)
args = parser.parse_args()

with open('./people.json') as chars:
    data = json.load(chars)
    myData = [['Index', 'Name', 'Height', 'Mass', 'Eyes']]
    for p in data:
        c = p['fields']
        new = [p['pk'], c['name'], c['height'], c['mass'], c['eye_color']]
        myData.append(new)

chcsv = open('./characters.csv', 'w', newline='')

with chcsv:
    writer = csv.writer(chcsv)
    writer.writerows(myData)

with open('characters.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    acc_total = -1 #because the first row is the headers
    acc_blue = 0
    for row in reader:
        acc_total += 1
        if row[4] == 'blue':
            acc_blue += 1
    perc = acc_blue/acc_total*100
    print(f"The percentage of Star Wars characters with blue eyes is: {perc:.2f}%.")

def removeUseless(S):
  """Removes spaces from a string.
  """
  if len(S) == 0:
    return ''
  if S[0] in '1234567890.':
    return S[0] + removeUseless(S[1:])
  else:
    return '' + removeUseless(S[1:])

def sortThird(val):
    if val[2] != 'unknown':
        return float(removeUseless(val[2]))
    else:
        return 10000

def sortFourth(val):
    if val[3] != 'unknown':
        return float(removeUseless(val[3]))
    else:
        return 10000

if args.sorting == "weight":
    with open('characters.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        read = []
        for row in reader:
            read.append(row)
        rest = read[1:] #don't grab the header line
        rest.sort(key = sortFourth)
        sortWeight = [read[0]] + rest
    y = read[0]
    print(str(y[0]).center(8), str(y[1]).rjust(22), str(y[2]).center(8), str(y[3]).center(10), str(y[4]).center(8))
    for x in rest:
        print(str(x[0]).center(8), str(x[1]).rjust(22), str(x[2]).center(8), str(x[3]).center(10), end=' ')
        print(str(x[4]).rjust(8))
elif args.sorting == "height":
    with open('characters.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        read = []
        for row in reader:
            read.append(row)
        rest = read[1:] #don't grab the header line
        rest.sort(key = sortThird)
    y = read[0]
    print(str(y[0]).center(8), str(y[1]).rjust(22), str(y[2]).center(8), str(y[3]).center(10), str(y[4]).center(8))
    for x in rest:
        print(str(x[0]).center(8), str(x[1]).rjust(22), str(x[2]).center(8), str(x[3]).center(10), end=' ')
        print(str(x[4]).rjust(8))
elif not args.sorting:
    # don't do anything
    time.sleep(0.01)
else:
    print("Not a valid argument for sorting.")

def inMovie(i, h):
    """Lists all the characters in a movie.
    """
    with open('./films.json') as filmchars:
        data = json.load(filmchars)
        charNums = []
        for p in data:
            if p["fields"]["episode_id"] == i:
                charNums.extend(p["fields"]["characters"])
                # map(lambda x: x -1, charNums) don't need this
    with open('./people.json') as people:
        data = json.load(people)
        movieChars = [['Index', 'Name', 'Height', 'Mass', 'Eyes']]
        for p in data:
            for i in range(len(charNums)):
                if p["pk"] == charNums[i]:
                    c = p['fields']
                    new = [p['pk'], c['name'], c['height'], c['mass'], c['eye_color']]
                    movieChars.append(new)
        y = movieChars[0]
        rest = movieChars[1:]
    if h == 'tall':
        rest.sort(key=sortThird, reverse=True)
    else:
        rest.sort(key = sortThird)
    print(str(y[0]).center(8), str(y[1]).rjust(22), str(y[2]).center(8), str(y[3]).center(10), str(y[4]).center(8))
    print(str(rest[0][0]).center(8), str(rest[0][1]).rjust(22), str(rest[0][2]).center(8), str(rest[0][3]).center(10), end=' ')
    print(str(rest[0][4]).rjust(8))

if args.tallest == str:
    inMovie(args.tallest, 'tall')
else:
    inMovie(args.shortest, 'short')