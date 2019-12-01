import sys, getopt

try:
  opts, args = getopt.getopt(sys.argv[1:], 'hHi:f:t:', [
    'from=', 'to=', 'input-file=', 'help',
  ])
except getopt.error as msg:
  print(msg)
  print("""\
  Help: python3 %s -h
  """%sys.argv[0])
  sys.exit(2)

from_character = ''
to_character = ''
plaintext = ''
filename = ''

for o, v in opts:
  if o in ('-h', '-H', '--help'):
    print((
      '\n'
      'Usage: python3 %s [options]'
      '\n\n'
      'Options:\n\n'
      '-f, --from          symbol or string\n'
      '-t, --to            symbol or string\n'
      '-i, --input-file    path to the file\n'
      '-h, --help          show help'
    )%sys.argv[0])
    sys.exit(0)
  if o in ('-f', '--from'):
    if len(v) == 0:
      print('Empty from option, see -h')
      sys.exit(1)
    from_character = v
  elif o in ('-t', '--to'):
    if len(v) == 0:
      print('Empty to option, see -h')
      sys.exit(1)
    to_character = v
  elif o in ('-i', '--input-file'):
    try:
      with open(v, 'r') as data:
        filename = v
        plaintext = data.read()
    except:
      print('Not found file "' + v + '"')
      sys.exit(1)

plaintext = plaintext.replace(from_character, to_character)

try:
  with open(filename, 'w') as file:
    file.write(plaintext)
except IOError as e:
  print(e)
  sys.exit(1)

print('Excellento')
sys.exit(0)