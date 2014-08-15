from stack import Stack

def baseConverter(decNumber, base):
  digits = "0123456789ABCDEF"

  remstack = Stack()
  
  while decNumber > 0:
    rem = decNumber % base
    remstack.push(rem)
    decNumber = decNumber // base

  newString = ""
  while not remstack.isEmpty():
    newString = newString + digits[remstack.pop()]

  return newString

# print baseConverter(25, 2) // -> 11001
# print baseConverter(25, 16) // -> 19

decNumber = input("Enter a decimal number: ")
base = input("Enter a base: ")
print baseConverter(decNumber, base)
