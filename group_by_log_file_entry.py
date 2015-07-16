from collections import Counter

def load_message(file_name):
    f = open(file_name, 'r')
    for line in f.readlines():
        yield line

def get_time_stamp():
    lm = load_message('./log_file')
    try:
        for msg in lm:
            msg_str = msg[:msg.find('fakehost')]
            yield msg_str[:msg_str.rfind(':')]
    except StopIteration, e:
        pass

ts_list = [ts for ts in get_time_stamp()]
print ts_list
ts_list.sort(key=lambda x: x[-6:])
print ts_list

print Counter(ts_list)

