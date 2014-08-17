from timeit import Timer

def empty():
  pass

t1 = Timer("empty()", "from __main__ import empty")

print t1.timeit(number=1000), "ms"
