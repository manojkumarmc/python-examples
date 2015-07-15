#! /usr/bin/python3

lst = []
for x in zip('Abcdefg', '42453565657'):
    lst.append(x)

print(lst)
print('*' * 100)

def sorter(atuple):
    return atuple[1]

lst1 = sorted(lst, key=sorter)

print(lst1)

