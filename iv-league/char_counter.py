from collections import Counter, OrderedDict
def count_chars(input_str):
    input_str = input_str.replace(' ','')
    ct = Counter(input_str)
    ol = OrderedDict.fromkeys(input_str)
    ret_str = ''
    for oi in ol:
        ret_str += (oi + str(ct[oi]))
    return ret_str

print count_chars('hey this is owesome or what thank you raymond for collections')

