import re

sentence = "I am flying out from BLR to DEL via MUM"
mtch = re.findall(r'\b[A-Z]{3}\b', sentence)
print mtch
