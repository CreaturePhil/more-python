import random
import time

this = {"one": 1, "two": 2, "three": 3}
static = {"this": this, this["three"]: "this"}
print "this - \t", this
print "static - \t", static
void = static
void[3] = {"this": this, "static": static, "void": "mindblow"}
print "static modified by void - \t", static

print this.keys()
print this.values()
print "one" in this

print this.items()

print '\n', '-'*10, '\n'

for (k, v) in void.items():
  print "HERE:", k, v

print '\n', '-'*10, '\n'

new = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(21):
  randstr = ''
  for r in range(6):
    randstr += alphabet[random.randint(0,24)]
  new[randstr] = random.randint(1, 10000) 

print new

# Random insertion sort appears!
def insertionsort(arr):
  start = time.time()
  for i in range(1, len(arr)):
    temp = arr[i]
    ci = i - 1
    while ci >= 0 and arr[ci] > temp:
      arr[ci+1] = arr[ci]
      ci = ci - 1
    arr[ci+1] = temp
  end = time.time()
  return end - start

print insertionsort(new.values()*200)
