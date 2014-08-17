print range(10)
print range(5, 10)
print range(1, 100, 2)

for number in range(5):
  print number + 1

stuff = ['123', 123, 'asdjlk', 'random']

for i in range(len(stuff)):
  print i, stuff[i]

vectors = []

for x in range(1, 11):
  for y in range(1, 11):
    vectors.append("(" + str(x) + "," + str(y) + ")")

print vectors
