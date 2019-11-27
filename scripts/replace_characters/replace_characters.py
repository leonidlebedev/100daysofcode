from_character = input('Change from: ')
to_character = input('Change to: ')
print('Change from «', from_character, '» to «', to_character, '»')
filename = input('Path to filename (\'example.txt\'): ')

try:
  with open(filename, 'r') as data:
    plaintext = data.read()
except:
  print('Not found file «', filename, '»')
  exit()


plaintext = plaintext.replace(from_character, to_character)

with open(filename, 'w') as file:
  file.write(plaintext)

print('Done')
