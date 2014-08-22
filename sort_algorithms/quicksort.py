from timeit import Timer
import random

def quickSort(alist):
  quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
  if first < last:
    splitpoint = partition(alist, first, last)

    quickSortHelper(alist, first, splitpoint - 1)
    quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
  pivotvalue = alist[first]
  
  leftmark = first + 1
  rightmark = last

  done = False
  while not done:
    while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
      leftmark = leftmark + 1

    while alist[rightmark] >= pivotvalue and rightmark >= leftmark :
      rightmark = rightmark - 1

    if rightmark < leftmark:
      done = True
    else:
      temp = alist[leftmark]
      alist[leftmark] = alist[rightmark]
      alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark

if __name__ == '__main__':
  alist = random.sample(xrange(100), 10)
  t1 = Timer("quickSort(alist)", "from __main__ import quickSort, quickSortHelper, partition, alist")
  print alist
  print t1.timeit(number=1000), "ms"
  print alist
