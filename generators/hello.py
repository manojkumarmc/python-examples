def sg():
    for x in range(5):
        y = yield x
        print(y)


s = sg()
s.send(None)
print(s.send("hi"))
