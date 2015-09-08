class Base(object):
    def add(self):
        print 'base add'

    def minus(self):
        print 'base minus'


class Op(Base):
    def add(self):
        super(Op, self).add()
        print 'Op add'

    def minus(self):
        super(Op, self).minus()
        print 'Op Minus'


op = Op()
op.add()
op.minus()
