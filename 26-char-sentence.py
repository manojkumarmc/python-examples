sen = "the quick brown fox jumps over the lazy dog"

dt = list(sorted(set(sen)))

for k,v in enumerate(dt):
    print ('{} {}'.format(k,v))
