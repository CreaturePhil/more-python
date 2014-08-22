from timeit import Timer
import random

def insertionSort(alist):
  for index in range(1, len(alist)):
    currentvalue = alist[index]
    position = index
    while position > 0 and alist[position-1] > currentvalue:
      alist[position] = alist[position-1]
      position = position - 1

    alist[position] = currentvalue

if __name__ == '__main__':
  alist = random.sample(xrange(100), 10)
  t1 = Timer("insertionSort(alist)", "from __main__ import insertionSort, alist")
  print alist
  print t1.timeit(number=1000), "ms"
  print alist
