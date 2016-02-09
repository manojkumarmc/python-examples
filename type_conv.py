import sys
import optparse

def decimal_converter(source, base):
  source = int(source)
  while source > 0:
    output.append(source % base)
    source = source // base
  pout = ''.join([str(i) for i in output[::-1]])
  return pout

def decimal_to_binary(source):
    return decimal_converter(source,2)

def binary_to_decimal(source):
  source = str(source)
  out_val = 0
  for k,v in enumerate(source[::-1]):
    out_val = out_val + int(v) * (2**int(k))
  return str(out_val)

def decimal_to_hexa(source):
    return decimal_converter(source, 16)

try:
  parser = optparse.OptionParser()
#  import pdb; pdb.set_trace()
  parser.add_option('-s', '--source', dest='source', help="The source value to convert", default="0")
  parser.add_option('-f', '--format', dest='format', help="The format of conversion. ['d2b', [b2d]", default="d2b")

  options, remainder = parser.parse_args()

  source = options.source
  output = []

  if options.format == 'd2b':
    print decimal_to_binary(source)
  elif options.format == 'b2d':
    print binary_to_decimal(source)
  elif options.format == 'd2x':
    print decimal_to_hexa(source)


  sys.exit(0)
except Exception, e:
  raise Exception(e)
  sys.exit(0)

