import operator

def splitter(al, l):
    ret_dict = {}
    for x in range(0, len(al)):
        sub_list = al[x: x + l]
        if len(sub_list) == l:
            ret_dict[x] = sum(sub_list)
    return ret_dict

def calculate(A, K, L):
    if type(K) != int or type(L) != int or type(A) != list:
        return -1

    if K == L:
        return -1

    if K < 0 or L < 0:
        return -1

    if len(A) < K or len(A) < L:
        return -1

    s1 = {x: sum(A[x: x + K]) for x in range(0, len(A)) if len(A[x:x+K]) == K}
    s2 = {x: sum(A[x: x + L]) for x in range(0, len(A)) if len(A[x:x+L]) == L}

    if K > L:
        large_range = K
        large_set = s1
        small_set = s2
    else:
        large_range = L
        large_set = s2
        small_set = s1

    # sorted_large_set = sorted(large_set.items(), key=operator.itemgetter(1))
    # sorted_small_set = sorted(small_set.items(), key=operator.itemgetter(1))
    sorted_large_set = sorted(large_set.items(), key=lambda x: x[1])
    sorted_small_set = sorted(small_set.items(), key=lambda x: x[1])

    lv = sorted_large_set.pop()
    for x in reversed(sorted_large_set):
        if x[1] < lv[1]:
            break
        lv = x

    ll = [x for x in reversed(sorted_small_set) if x[0] < lv[0] or x[0] > (lv[0] + large_range - 1)]

    return lv[1] + ll[0][1]



al = [6,1,4,6,3,2,7,4]

print(calculate(al,3,2))
print(calculate(al,-3,2))
print(calculate(al,3,10))
