
def time_converter(time_str):
    time_str = time_str.rjust(4,'0')
    if time_str[-2:] == 'PM':
        return str(int(time_str[0:2]) + 12) + time_str[2:len(time_str) - 2]
    else:
        return time_str.replace('PM', '').replace('AM', '')


# if __name__ == "__main__":
#     print time_converter('1AM')
