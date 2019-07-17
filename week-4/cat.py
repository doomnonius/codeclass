import argparse
import json
import re


parser = argparse.ArgumentParser()
parser.add_argument("cat", help="reads and prints the contents of any file passed as its argument")
args = parser.parse_args()

inp = args.cat

with open(inp) as doc:
    data = doc.read()
    # for line in data:
    regex = r"\+?\n?(\d+?)\n?(\d*)\n?[\.\s-]?\n?\(?(\d+)\n?(\d+)\n?(\d+)\)?[\s\.-]?\n?(\d+)\n?(\d+)\n?(\d+)[\s\.-]?(\d+)\n?(\d+)\n?(\d+)\n?(\d+)"
    matchList = re.finditer(regex, data)
    for match in matchList:
        print("+{0}{1} ({2}{3}{4}) {5}{6}{7}-{8}{9}{10}{11}".format((match.group(1)), (match.group(2)), (match.group(3)), (match.group(4)), (match.group(5)), (match.group(6)), (match.group(7)), (match.group(8)), (match.group(9)), (match.group(10)), (match.group(11)), (match.group(12))))