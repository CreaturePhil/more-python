class Stack:

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    return self.items.append(item)

  def pop(self):
    return self.items.pop()
  
  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

# s = Stack()

# # print s.isEmpty() // -> True
# s.push(100)
# s.push('Google.com')
# # print s.peek() // -> 'Google.com'
# s.push(True)
# # print s.size() // -> 3
# print s.isEmpty() // -> False
# s.push(1829.2)
# print s.pop() // -> 1829.2
# print s.pop() // -> True
# print s.size() // -> 2
