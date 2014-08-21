import time

def complex_computation(a, b):
  time.sleep(.5)
  return a + b

cache = {}
def cached_computation(a, b):
  key = (a, b)
  if key in cache:
    r = cache[key]
  else:
    r = complex_computation(a, b)
    cache[key] = r

  return r

start_time = time.time()
print cached_computation(5, 3)
print "The first computation took %f seconds" % (time.time() - start_time)

start_time2 = time.time()
print cached_computation(5, 3)
print "The second computation took %f seconds" % (time.time() - start_time2)
