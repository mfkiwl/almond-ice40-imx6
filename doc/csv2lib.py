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
        starty = y
        for pin in pins:
            y -= 100
            print("X %s %s 0 %d 100 R 40 50 %d 1 I" % (pin[0], pin[1], y, groupno))
        if power_group:
            mid = (starty - 100 + y) // 2
            print("T 900 -150 %d 50 0 %d 1 %s Normal 0 C C" % ((mid, groupno, power_group)))
            print("P 4 %(group)d 1 20 -50 %(start)d -100 %(start)d -100 %(end)d -50 %(end)d N" % {'group': groupno, 'start': starty - 50, 'end': y - 50})
        y -= 100
