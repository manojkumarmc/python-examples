
"""
This is a method to display the concent of closure
"""
def mather(a,b):
    def add():
        return a + b
    def mul():
        return a * b
    def div():
        return a / b

    return {
        'add' : add,
        'mul' : mul,
        'div' : div
    }


o = mather(2,3)
print o['add']()
print o['mul']()
print o['div']()

print 20 * "="
"""
Another simple example
"""

def summer(x):
    def add(y):
        return x + y
    return add

s = summer(10)
print s(2)
