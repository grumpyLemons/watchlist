# Made by me

import argparse
import json
import random


def add(movie):
    watchlist.append(movie)
    d_file = open('movies.json', 'w')
    json.dump(watchlist, file)
    d_file.close()


def remove(movie):
    watchlist.pop(watchlist.find(movie))
    d_file = open('movies.json', 'w')
    json.dump(watchlist, file)
    d_file.close()


file = open('movies.json', 'r')
watchlist = json.load(file)
watchlist = list(set(watchlist))
file.close()

parser = argparse.ArgumentParser(description='Watchlist')
parser.add_argument("-a", "--add", help="Add movie to the watchlist")
parser.add_argument("-r", "--rm", help="Removes movie from the watchlist")
args = parser.parse_args()

try:
    if args.add:
        add(args.add)
    elif args.rm:
        remove(args.rm)
    else:
        print(random.choice(watchlist))
except PermissionError:
    print('permission err')
