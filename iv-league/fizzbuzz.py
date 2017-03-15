'''
This is a simple program which prints
FizzBuzz = divisible by 3 and 5
Fizz = divisible by 3
Buzz = divisible by 5
else print the number
'''

def is_factor(num, factor):
    return num % factor == 0

for x in range(1,50):
    f3 = is_factor(x,3)
    f5 = is_factor(x,5)
    if f3 and f5:
        print "FizzBuzz"
    elif f3 and not f5:
        print "Fiz"
    elif f5 and not f3:
        print "Buzz"
    else:
        print x
