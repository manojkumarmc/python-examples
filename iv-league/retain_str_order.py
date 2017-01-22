class MyCounter():
    def __init__(self, in_str):
        self._in_str = in_str
        try:
            self._ol = [(in_str[0],0)]
        except:
            raise Exception('The string you entered is invalid')

    def upsert_data(self, c):
        for k,v in enumerate(self._ol):
            v1, v2 = v
            is_found = False
            if v1 == c:
                v2 += 1
                self._ol[k] = (v1,v2)
                is_found = True
        if not is_found:
            self._ol.append((c, 1))

    def do_process(self):
        for c in self._in_str:
            self.upsert_data(c)

    def get_data_dict(self):
        return self._ol

    def __str__(self):
        return str(self._ol)


mc = MyCounter('aaaaaxxxaaaassdddddtuv')
mc.do_process()
ctr_dict =  mc.get_data_dict()

final_format = ''
for k,v in enumerate(ctr_dict):
    x,y =  v
    if y == 1:
        final_format += x
    else:
        final_format += (x + str(y))

print final_format
