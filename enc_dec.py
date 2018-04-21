def encr(in_str):
    chr_map = [str(ord(x)).rjust(4, '0') for x in in_str ]
    return ''.join ([x[::-1] for x in chr_map])


def decr(in_str):
    tot_char = int(len(in_str)/4)
    out_ary = []
    start = 0
    end = 4
    for x in range(tot_char):
        out_ary.append(in_str[start:end])
        start += 4
        end += 4
    return ''.join(chr(int(w[::-1])) for w in out_ary)



def main():
    #ew = encr('hello there')
    ew = encr('hello')
    print (ew)
    dw = decr(ew)
    print(dw)


if __name__ == "__main__":
    main()
