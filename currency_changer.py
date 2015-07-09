import collections
import pprint

def changer(amt):
    change = collections.OrderedDict()
    currencies = (1000.00, 500.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50)
    for c in currencies:
        if amt > 0:
            divs = amt // c
            if divs >= 1:
                amt = amt - divs * c
                change[c] = int(divs)

    for p in change:
        print p


changer(78)        
