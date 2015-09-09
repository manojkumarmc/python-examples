

class _ST(object):
    def __init__(self):
        self.instance = "Instance at %d" % self.__hash__()

_st = _ST()
        
def ST():
    return _st
        
st = ST()
print st.instance
st._msg = 'Hello there'

st1 = ST()
print st1.instance
print st1._msg



        
        
