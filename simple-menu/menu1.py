start_val = False

while True:
    print "[Press 1 to Start]"
    print "[Press 2 to Continue]"
    print "[Press 3 to Stop]"
    print "--------------------------------"
    inp = raw_input('Enter your value :')
    if not start_val:
      if int(inp) != 1:
          print "Cant start without 1"
      else:
          start_val = True
    else:
        if int(inp) == 2:
            print "Continuing"
        elif int(inp) == 3:
            print "Stopping"
            break