list1 = [23, "sadjl", [23, 3, 12.2], "hoe", (2,4), "power", 5.2]
print 'hoe' in list1
print list1 * 3
print list1[:]
print list1[-3:]
print list1[1:5]
list2 = list1
list2[0] = "DESTROY"
print list1 is list2
print list1
a = [1]
b = [1]
print a is b
for i in range(10):
  a.append(i)
print a
a.insert(0, "sup")
a.pop()
print a
print [i ** 2 for i in a if type(i) == type(1) and i%2 == 0]
