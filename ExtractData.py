"""Export data from several json files to a single csv file"""

import json
import csv
from os import listdir
from os.path import exists, isdir, join


def main():
    path = "data"
    players = []

    """create an output file is it does not exists"""
    if not exists('{}\players_output.csv'.format(path)):
        with open('{}\players_output.csv'.format(path), 'w', newline='') as csvfile:
            fieldnames = ['source', 'id', 'name', 'plays']
            writer = csv.DictWriter(csvfile, extrasaction='ignore', fieldnames=fieldnames)
            writer.writeheader()

    """search for the file 'players.json' inside each folder"""
    for p in listdir(path):
        if isdir(join(path, p)):
            for f in listdir(join(path, p)):
                if f == "players.json":
                    players.append(read_json(join(path, p, f)))

                    with open('{}\players_output.csv'.format(path), 'a', newline='') as csvfile:
                        fieldnames = ['source', 'id', 'name', 'plays']
                        writer = csv.DictWriter(csvfile, extrasaction='ignore', fieldnames=fieldnames)
                        for i in players:
                            for key in i:
                                players[0][key]['source'] = p
                                writer.writerow(players[0][key])
                    players.clear()


def read_json(folder):
    with open(folder, 'r', encoding='utf8') as f:
        return json.load(f)


if __name__ == "__main__":
    main()
