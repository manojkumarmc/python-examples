from operator import itemgetter

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

# while True:
#     print "1. Continue"
#     print "2. Exit"
#     print "_______________"
#     s = raw_input('Please enter your value: ')
#     if str(s).strip() != '2':
#         print 'You entered %s ' % str(s)
#     else:
#         print "Exiting"
#         break

# print(sort_the_list(1))
# print(sl(2))


