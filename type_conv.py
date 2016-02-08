import sys
import optparse

def decimal_to_binary(source):
  source = int(source)
  while source > 0:
    output.append(source % 2)
    source = source // 2
  pout = ''.join([str(i) for i in output[::-1]])
  return pout

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
    print 'aha'


  sys.exit(0)
except Exception, e:
  raise Exception(e)
  sys.exit(0)

