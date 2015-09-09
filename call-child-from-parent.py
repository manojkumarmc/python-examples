class Parent(object):
  def mth1(self):
    return 'mth1 ' + self.mth2()


class Child(Parent):
  def mth2(self):
    return 'mth2'


c = Child()
print c.mth1()
