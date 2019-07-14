import argparse
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--crawl", help="enter an episode number to display its text crawl", type=int)
args = parser.parse_args()

with open('./films.json') as films:
    data = json.load(films)
    for p in data:
        if p['fields']['episode_id'] == args.crawl:
            craw = p['fields']['opening_crawl'].split(sep="\r\n")
            print(len(craw))
            for line in craw:
                print(f'{line}'.center(80))
                time.sleep(0.5)
            break
