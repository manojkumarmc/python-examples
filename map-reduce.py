
class MyBase(object):

    """Docstring for MyBase. """

    def __init__(self, name):
        """TODO: to be defined1.

        :name: TODO

        """
        self._name = name

    def get_found_properties(self, properties):
        property_items = map(lambda x: (x, getattr(self, x, None)), properties)
        return dict(filter(lambda x: x[1], property_items))

class Child(MyBase):

    def __init__(self):
       pass

    @property
    def p1(self):
        return 'p1'

    @property
    def foo(self):
        return 1

cl = Child()
print cl.get_found_properties(['p1','second','foo'])

