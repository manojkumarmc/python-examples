import pprint

input_list = [
    'day,hour,second,minute',
    'day = 24 hour',
    'hour = 60 minute',
    'minute = 60 second'
]

output = '1 day == 24 hour == 1440 minute == 86400 second'

units_str = input_list[0]
units = {}

for u in units_str.split(','):
    units[u] = None

input_list.pop(0)

for il in input_list:
    lo = il.split('=')
    key =  lo[0].strip()
    value = lo[1].strip()
    vd = value.split(' ')
    units[key] = {'key': vd[0], 'value': vd[1]}

for k in units.iterkeys():
    if units[k] == None:
        smallest = k

def printer(value):
    while True:
        out = ''
        for k in units.keys():
            if units[k]['value'] == value:
                out =  k, units[k]['key'], value
                yield out
                value = k

        if out == '':
            raise StopIteration


units.pop(smallest)

out_lst = []
for x in printer(smallest):
    out_lst.append(x)

'''
('day', '24', 'hour')
('hour', '60', 'minute')
('minute', '60', 'second')
'''

ctr = 1
out_str = ''
for r in reversed(out_lst):
    if ctr == 1:
        out_str += r[0] + ' == ' + str(ctr * int(r[1])) + ' ' + r[2]
    else:
        out_str += ' == ' + str(ctr * int(r[1])) + ' ' + r[2]
    ctr *= int(r[1])


print out_str
