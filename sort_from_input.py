from operator import itemgetter
import re

to_sort_list = []
sort_key = 0

def sort_the_list(sort_key=0):
    return sorted(to_sort_list, key=lambda row: row[sort_key])

def sl(sort_key=0):
    return sorted(to_sort_list, key=itemgetter(sort_key))

def sanitize_number(a_str):
    return tuple(re.findall(r'\d+',a_str))

while True:
    print "1. Add numbers differenciated with space"
    print "2. Sort the table"
    print "3. Exit"
    print "_______________"
    s = raw_input('Please enter your value: ')
    key_entered = str(s).strip()
    if key_entered == '1':
        print ""
        s1 = raw_input("Enter values: ")
        print 'You entered %s ' % str(s1)
        to_sort_list.append(sanitize_number(s1))
    elif key_entered == '2':
        print sl()
    else:
        print "Exiting"
        break


