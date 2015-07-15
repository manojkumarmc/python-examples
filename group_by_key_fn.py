#! /usr/bin/python3

from itertools import groupby

lst = []
for x in zip('Abcdefg', '42453565657'):
    lst.append(x)

print(lst)
print('*' * 100)

def sorter(atuple):
    return atuple[1]

lst1 = sorted(lst, key=sorter)

print(lst1)

groups = []
uniquekeys = []
for k,g in groupby(lst, sorter):
    groups.append(list(g))
    uniquekeys.append(k)

print('*' * 100)
print(groups)
print(uniquekeys)
