import re

SENTENCE = "I am flying out from BLR to DEL via MUM"


def list_airports(stnce):
    mtch = re.findall(r'\b[A-Z]{3}\b', stnce)
    return mtch

# if __name__ == "__main__":
#     print list_airports(SENTENCE)

# ['BLR', 'DEL', 'MUM']
