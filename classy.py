class MyClass(object):
    def __new__(cls, *args, **kwargs):
        obj = super(MyClass, cls).__new__(cls)
        print "object created"
        return obj

    def __init__(self, name):
        print "init method called"
        self.name = name

    def __del__(self):
        print "del mehtod called"



mc = MyClass('its me')
print mc.name

        
        
