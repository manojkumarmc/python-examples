from itertools import groupby
from pprint import pprint

my_list = [
    {'id' : 1, 'name' : 'manoj'},
    {'id' : 1, 'email' : 'manoj@chumma.com'},
    {'id' : 2, 'name' : 'kumar'},
    {'id' : 2, 'email' : 'kumar@chumma.com'},
    ]

myd = [dict(
    reduce(lambda y,z: y+z, 
      map(lambda x:x.items(),v)
      )
    ) for k,v in groupby(my_list, key=lambda x: x['id'])] 

pprint(myd)

