"""
So the jist is...

if a variable is operated upon inside a function, it is assumed global
until, that is a big until, any assignment is made to it

if an assignment is made against a variable name, a new local object will be created.

hence in the function method() is able to change an immutable string object

"""


astring = "Hello There"

def liner():
    print "=" * 20
    
# string is immutable so pass by value ??
def method(s):
    print "got " + s
    s =  "I am changing it"
    print s

method(astring)

print "after call "
liner()
print astring

liner()
alist = ['item1', 'item2']

def method1(lst):
    print 'got list ' + str(lst) 
    lst.append('item3')
    print 'after addition ' + str(lst)

method1(alist)
print 'after call '
liner()
print alist


liner()

atuple = ('Value1', 'Value2')
def method2(tup):
    try:
        print "Got " + str(tup)
        tup[0] = 'Trying to change'
        print "after addition " + str(tup)
    except Exception, ex:
        print ex
        


method2(atuple)
print 'after call'
liner()
print atuple


liner()
tup1 = (5,6,7)
def method3(tup):
    print 'got ' + str(tup)
    tup = (1,2)
    print 'after changing ' + str(tup)

method3(tup1)
print 'after call'
liner()
print tup1

'''
got Hello There
I am changing it
after call 
====================
Hello There
====================
got list ['item1', 'item2']
after addition ['item1', 'item2', 'item3']
after call 
====================
['item1', 'item2', 'item3']
====================
Got ('Value1', 'Value2')
'tuple' object does not support item assignment
after call
====================
('Value1', 'Value2')
====================
got (5, 6, 7)
after changing (1, 2)
after call
====================
(5, 6, 7)

'''





 

    
    
