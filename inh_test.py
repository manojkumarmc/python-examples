class Base(object):
    def __init__(self):
        print "init from base"
        
    def add(self):
        print 'base add'

    def minus(self):
        print 'base minus'


class Op(Base):
    def __init__(self):
        super(Op, self).__init__()
        print "init from child"
        
    def add(self):
        super(Op, self).add()
        print 'Op add'

    def minus(self):
        super(Op, self).minus()
        print 'Op Minus'


op = Op()
op.add()
op.minus()
