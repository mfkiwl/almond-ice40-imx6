import csv
import argparse
import itertools

def groupby(iter, fn):
    return itertools.groupby(sorted(iter, key=fn), fn)

parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType('r', encoding='utf-8'))
args = parser.parse_args()

data = [list(row) for row in csv.reader(args.file)]

pins = []

for row in data[1:]:
    cordy = row[0]
    for pin, cordx in zip(row[1:], data[0][1:]):
        pins.append((cordy+cordx, pin))

y = 0
for group, pins in groupby(pins, lambda p: p[1]):
    for pin in pins:
        y -= 100
        pintype = 'I'
        if pin[1][0] == 'V':
            pintype = 'W'
        print("X %s %s 0 %d 150 R 40 50 0 1 %s" % (pin[1], pin[0], y, pintype))
