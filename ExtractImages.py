"""Export the images in png format from base64 images inside a json file
Export the images base64 from json files to a single csv file"""

import json
import csv
from os import listdir
from os.path import exists, isdir, join
import base64


def main():
    path = "data"
    players = []

    """create the output file if does not exists"""
    if not exists('{}\players_picture_output.csv'.format(path)):
        with open('{}\players_picture_output.csv'.format(path), 'w', newline='') as csvfile:
            fieldnames = ['source', 'id', 'picture']
            writer = csv.DictWriter(csvfile, extrasaction='ignore', fieldnames=fieldnames)
            writer.writeheader()

    """Search for 'players.json' file inside each folder"""
    for p in listdir(path):
        if isdir(join(path, p)):
            for f in listdir(join(path, p)):
                if f == "players.json":
                    players.append(read_json(join(path, p, f)))

                    """Loop to insert rows and exportation of images"""
                    for i in players:
                        for key in i:
                            """insert rows with image base64 into csv file"""
                            players[0][key]['source'] = p
                            row = players[0][key]
                            image_csv = '{}\players_image_output.csv'.format(path)
                            insert_row(row, image_csv)

                            """exportar imagem base64 em png"""
                            image_encoded = players[0][key]['picture'].split(',')[1]
                            image_file = '{}/image/{}_{}_image.png'.format(path, p, players[0][key]['id'])
                            decode_image(image_encoded, image_file)

                    players.clear()


def read_json(file):
    with open(file, 'r', encoding='utf8') as f:
        return json.load(f)


def insert_row(row, file):
    with open(file, 'a', newline='') as csvfile:
        fieldnames = ['source', 'id', 'picture']
        writer = csv.DictWriter(csvfile, extrasaction='ignore', fieldnames=fieldnames)
        writer.writerow(row)


def decode_image(image_encoded, file):
    image_64_decode = base64.b64decode(image_encoded)
    with open(file, 'wb') as f:
        f.write(image_64_decode)


if __name__ == "__main__":
    main()
