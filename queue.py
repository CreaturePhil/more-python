class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

# q= Queue()
# print q.isEmpty() // -> True

# q.enqueue('dog')
# q.enqueue(4)
# print q.size() // -> 2
# q= Queue()
# print q.isEmpty() // -> True

# q.enqueue('stuff')
# q.enqueue('dog')
# q.enqueue(False)
# print q.size() // -> 3
# print q.dequeue() // -> stuff
# print q.size() // -> 2
