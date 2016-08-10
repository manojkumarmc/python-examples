def mthd1(p1, p2=None, verify=False):
    mthd2(verify=verify)


def mthd2(verify):
    print(verify)

def tx_data(url, data, killswitch=None, verify=False,  **kwargs):
    print(url)
    print(data)
    print(killswitch)
    print(verify)
    print(kwargs)

def m3(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == '__main__':
    # mthd1(1, 'something', True)
    # tx_data('url','data', 'killswitch', verify='Hoo', test=1, test1=3)
    m3(1,2,hello=1,there=2)


