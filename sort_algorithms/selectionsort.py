from timeit import Timer
import random

def selectionSort(alist):
  for fillslot in range(len(alist) - 1, 0, -1):
    positionOfMax = 0
    for location in range(1, fillslot+1):
      if alist[location] > alist[positionOfMax]:
        positionOfMax = location

    temp = alist[fillslot]
    alist[fillslot] = alist[positionOfMax]
    alist[positionOfMax] = temp

if __name__ == '__main__':
  alist = random.sample(xrange(100), 10)
  t1 = Timer("selectionSort(alist)", "from __main__ import selectionSort, alist")
  print alist
  print t1.timeit(number=1000), "ms"
  print alist
