import re

def get_extension(file_name):
    out = re.search(r'(\.(.+))$', file_name)
    print out.groups()

get_extension('filename.jpeg')
get_extension('filename.jpeg.txt')

