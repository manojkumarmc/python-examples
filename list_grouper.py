from operator import itemgetter
from itertools import groupby

alist = ['abc', 'bac', 'cab', '1234', '4321', 'ab', 'xy', 'ba']

tlist = [(''.join(sorted(list(x))),x)for x in alist]
tlist.sort(key=itemgetter(0))
print tlist

groups = groupby(tlist, itemgetter(0))
for key,data in groups:
    print key
    for item in data:
        print item



    
