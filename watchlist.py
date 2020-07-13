# Made by me

import argparse
import json
import random
from string import capwords


def add(movies):
    for movie in ' '.join(movies).split('; '):
        watchlist.append(capwords(movie))
    d_file = open('movies.json', 'w')
    json.dump(watchlist, d_file)
    d_file.close()


def remove(movies):
    for movie in ' '.join(movies).split('; '):
        try:
            watchlist.pop(watchlist.index(capwords(movie)))
        except (ValueError):
            print(f"There is no movie called {movie}")

    d_file = open('movies.json', 'w')
    json.dump(watchlist, d_file)
    d_file.close()


def listm():
    for movie in watchlist:
        print(movie)


file = open('movies.json', 'r')
watchlist = json.load(file)
watchlist = sorted(list(set(watchlist)))
file.close()

parser = argparse.ArgumentParser(description='Watchlist')
parser.add_argument(
    "-a", "--add", help="Add movie to the watchlist", nargs='*')
parser.add_argument(
    "-r", "--rm", help="Removes movie from the watchlist", nargs='*')
parser.add_argument(
    "-l", "--list", help="Lists all movies from the list", action='store_true')
args = parser.parse_args()
try:
    if args.add:
        add(args.add)
    elif args.rm:
        remove(args.rm)
    elif args.list:
        listm()
    else:
        print(random.choice(watchlist))
except (PermissionError, IndexError):
    pass
