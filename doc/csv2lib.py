import csv
import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType('r', encoding='utf-8'))
args = parser.parse_args()

# skip header
args.file.readline()
data = csv.reader(args.file)

def groupby(iter, fn):
    return itertools.groupby(sorted(iter, key=fn), fn)

groupno = 0
for group, pins in groupby(data, lambda row: row[9]):
    groupno += 1
    y = 0
    print("T 0 0 %d 100 0 %d 1 %s Italic 0 C C" % (y, groupno, group))
    y -= 100
    for power_group, pins in groupby(pins, lambda row: row[2]):
        if power_group:
            y -= 100
            print("T 0 0 %d 50 0 %d 1 %s Normal 0 C C" % (y, groupno, power_group))
        for pin in pins:
            y -= 100
            print("X %s %s 0 %d 100 R 40 50 %d 1 I" % (pin[0], pin[1], y, groupno))
