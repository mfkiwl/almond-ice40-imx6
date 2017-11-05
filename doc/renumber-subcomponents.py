import sys
import re
import argparse

mapping = {}
for e in sys.argv[1:]:
    e = e.split(',')
    mapping[e[0]] = e[1]

def renumber(n):
    return mapping[n]

for line in sys.stdin.readlines():
    line = line.strip()
    elm = line.split()
    if elm[0] == 'T':
        elm[6] = renumber(elm[6])
    elif elm[0] == 'S':
        elm[5] = renumber(elm[5])
    elif elm[0] == 'P':
        elm[2] = renumber(elm[2])
    elif elm[0] == 'X':
        elm[9] = renumber(elm[9])
    line = " ".join(elm)
    print(line)
