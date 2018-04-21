
PAD_KEY = 4

def encr(in_str):
    chr_map = [str(ord(x)).rjust(PAD_KEY, '0') for x in in_str ]
    return ''.join(chr_map[::-1])


def decr(in_str):
    tot_char = int(len(in_str)/PAD_KEY)
    out_ary = []
    start = 0
    end = PAD_KEY
    for x in range(tot_char):
        pad_str = in_str[start:end]
        out_ary.append(pad_str)
        start += PAD_KEY
        end += PAD_KEY
    return ''.join(chr(int(x)) for x in reversed(out_ary))



def main():
    ew = encr('manoj kumar mc')
    print (ew)
    dw = decr(ew)
    print(dw)
#
#
# if __name__ == "__main__":
#     main()
