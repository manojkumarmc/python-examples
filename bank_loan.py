#! /usr/bin/python3

import sys
import optparse

def list_outstanding(principal=0, emi=0, years=0):
    ctr = 1
    total_interest = 0
    total_emi = 0
    #year_months = 12 * years
    year_months = 122
    print '================================================'
    print '{0} | {1} | {2} | {3}'.format('SlNo', 'Outstanding', 'Interest', 'Principal')
    print '================================================'
    while principal > 0:
        interest = (principal * 0.1020) // 12
        emi_to_pay = emi - interest
        print '{0:>4}  {1:>.2f}  {2:.2f}  {3:.2f}'.format(ctr, principal, interest, emi_to_pay)
        total_interest += interest
        total_emi += emi_to_pay
        ctr += 1
        principal -= emi_to_pay
        if ctr > year_months:
            break

    print '==============================================='
    print 'Total EMI paid : {0:.2f} \nTotal Interest Paid : {1:.2f}'.format(total_emi, total_interest)
    print 'Final Pay : {0:.2f}'.format(total_emi + total_interest)
    print '==============================================='


def main(argv):
    try:
        parser = optparse.OptionParser()
        parser.add_option('-p', '--principal', dest="principal", help="Principal Amt.", default=0,)
        parser.add_option('-e', '--emi', dest="emi", help="EMI per month.", default=0,)
        parser.add_option('-y', '--years', dest="years", help="Years of pay.", default=0,)
        options, remainder = parser.parse_args()

        list_outstanding(principal=float(options.principal), emi=float(options.emi), years=int(options.years))
        sys.exit(0)
    except Exception, e:
        raise Exception(e)
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])

        