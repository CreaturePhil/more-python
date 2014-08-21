import random

def sequentialSearch(alist, item):
  pos = 0
  found = False

  while pos < len(alist) and not found:
    if alist[pos] == item:
      found = True
    else:
      pos = pos + 1

  return found

testList = random.sample(xrange(100), 20)
ranNum = random.randrange(0, 100)
ranNumFromList = random.choice(testList)
print testList
print ranNum, sequentialSearch(testList, ranNum)
print ranNumFromList, sequentialSearch(testList, ranNumFromList)
testList.sort()
print testList

def binarySearch(alist, item):
  if len(alist) == 0:
    return False
  else:
    midpoint = len(alist) / 2
    if alist[midpoint] == item:
      return True
    else:
      if item < alist[midpoint]:
        return binarySearch(alist[:midpoint], item)
      else:
        return binarySearch(alist[midpoint+1:], item)

print ranNum, binarySearch(testList, ranNum)
print ranNumFromList, binarySearch(testList, ranNumFromList)
