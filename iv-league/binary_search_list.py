import bisect

alist = [1,1,1,3,3,3,5,5,8,8,8,8,9,9,9]

def get_count(num):
    return bisect.bisect_right(alist, num) - bisect.bisect_left(alist, num)

print get_count(3)
print get_count(8)

