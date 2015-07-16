
from itertools import groupby

alist = ['abc', 'bac', 'cab', '1234', '4321', 'ab', 'xy', 'ba']

groups = groupby(alist, key=lambda x: ''.join(sorted(list(x))))
output = dict()

#for key, data in groups:
#    print key
#    for item in data:
#        print item

for key,data in groups:
    oitem = ''
    for item in data:
        oitem += item + ' '
    output[item] = oitem
    
print output



    
