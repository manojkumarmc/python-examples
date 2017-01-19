from operator import itemgetter
import re

to_sort_list = [
    (10, 2, 9),
    (8, 8, 8),
    (12, 5, 4),
    (1, 1, 1)
]

sort_key = 0

def sort_the_list(sort_key=0):
    return sorted(to_sort_list, key=lambda row: row[sort_key])

def sl(sort_key=0):
    return sorted(to_sort_list, key=itemgetter(sort_key))

def sanitize_number(a_str):
    return re.findall(r'\d+',a_str)

while True:
    print "1. Add numbers differenciated with space"
    print "2. Sort the table"
    print "3. Exit"
    print "_______________"
    s = raw_input('Please enter your value: ')
    if str(s).strip() != '3':
        print ""
        s1 = raw_input("Enter values: ")
        print 'You entered %s ' % str(s1)
    else:
        print "Exiting"
        break

# print(sort_the_list(1))
# print(sl(2))

# print(tuple(sanitize_number('is 100 greater than 9')))

