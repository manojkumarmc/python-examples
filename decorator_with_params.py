from functools import wraps

def my_decorator(param1="", param2=""):
    def inner1(fn):
        @wraps(fn)
        def inner2(*args, **kwargs):
            print "The callee is " + fn.__name__
            print "Info on method " + fn.__doc__
            if param1.strip() != "":
                print "Param1 : " +  param1
            if param2.strip() != "":
                print "Param2 : " + param2
            return fn(*args, **kwargs)
        return inner2
    return inner1


@my_decorator(param1="First")
def my_method1():
    '''
    This will illustrate the doc var inside the decorator
    '''
    print "hello from my_method1"


@my_decorator(param2="Second")
def my_method2():
    '''
    Again the proof of doc var
    '''
    print "hellp from my_method2"


my_method1()
my_method2()



