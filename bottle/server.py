from bottle import Bottle, run, route
from functools import wraps
from  bottle_redis import RedisPlugin

app = Bottle()
plugin = RedisPlugin(host='localhost')
app.install(plugin)


def my_dec(fn):
    @wraps(fn)
    def meth1(*args, **kwargs):
        print fn
        print("something gotta give")
        f = fn(*args, **kwargs)
        return f
    return meth1

@route('/hello')
#@my_dec
def hello(rdb):
    rdb.set('test',1)
    return "Hello World!"

run(host='localhost', port=9090, debug=True)
