import math

print "n", "\t", "n**2", "\t", "n log n", "\t", "log n"
print "---", "\t", "----", "\t", "-"*7, "\t", "-"*5

for n in range(1, 13):
  if n == 1:
    print n, "\t", n**2, "\t", n * math.log(n), "\t\t", math.log(n)
  else:
    print n, "\t", n**2, "\t", n * math.log(n), "\t", math.log(n)
