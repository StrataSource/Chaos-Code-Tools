#!/usr/bin/env python3

import os, sys

lines = []
with open("vpc-keywords.txt") as fp:
    lines = fp.readlines()

# sort alphabetical
lines = sorted(lines)
# sort w/length
def k(s):
    return -len(s),s
lines = sorted(lines, key=k)

outlines = []
for line in lines:
    if len(line) <= 0 or line.isspace():
        continue
    if line.startswith('#'):
        continue
    l = ""
    for c in line:
        if c == '\n':
            break
        if c == '$':
            l += '\\\\' + c
            continue
        if c.isupper():
            l += '[' + c + c.lower() + ']'
            continue
        l+=c 
    outlines.append(l)

print('(', end='')
for l in outlines:
    print(l, end='|')
print(outlines[0] + ')')


