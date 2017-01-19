
while True:
    print "1. Continue"
    print "2. Exit"
    print "_______________"
    s = raw_input('Please enter your value: ')
    if str(s).strip() != '2':
        print 'You entered %s ' % str(s)
    else:
        print "Exiting"
        break
