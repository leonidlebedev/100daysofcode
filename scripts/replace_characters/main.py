import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], 'h:', [
  'from=', 'to=', 'input-file='
])

from_character = '.'
to_character = ','
plaintext = None
filename = None

for o, v in opts:
  if o == '--from':
    if len(v) == 0:
      print('Empty from option, see -h')
      sys.exit(1)
    from_character = v
  elif o == '--to':
    if len(v) == 0:
      print('Empty to option, see -h')
      sys.exit(1)
    to_character = v
  elif o == '--input-file':
    try:
      with open(v, 'r') as data:
        filename = v
        plaintext = data.read()
    except:
      print('Not found file "' + v + '"')
      sys.exit(1)

plaintext = plaintext.replace(from_character, to_character)

with open(filename, 'w') as file:
  file.write(plaintext)

print('Excellento')
sys.exit(0)