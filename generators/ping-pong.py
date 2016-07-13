def my_gen():
    """TODO: Docstring for my_gen.
    :returns: TODO

    """
    for x in range(10):
        print("from gen {}".format(x))
        yield x

mg = my_gen()
mg.send(None)

try:
    while True:
        print("from while {}".format(mg.send(1)))
except Exception as e:
   pass
