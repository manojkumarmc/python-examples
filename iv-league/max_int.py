from itertools import permutations


def max_int(input):
    diff = 0
    n_max = 0
    __import__('pdb').set_trace()
    for x in permutations(str(input), len(str(input))):
        t_int = int(''.join(x))
        if t_int > input:
            print '* ' + str(t_int)
            if diff == 0:
                n_max = t_int
                diff = t_int - input
            else:
                if diff < (t_int - input):
                    diff = (t_int - input)
                    n_max = t_int
    print n_max



# max_int(12)
# max_int(513)
max_int(2017)
