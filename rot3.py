def rot3(mess):
  mess =  mess.lower() 
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted = ''
  for char in mess:
    if char == ' ':
      encrypted = encrypted + ' '
    else:
      rotated_index = alphabet.index(char) + 13
      if rotated_index < 26:
        encrypted = encrypted + alphabet[rotated_index]
      else:
        encrypted = encrypted + alphabet[rotated_index % 26]
  return encrypted

name = rot3("Philip La")
print name
print rot3(name)

print rot3("This is a secret message")
