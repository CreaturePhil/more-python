# Functions
def foo():
  return 1

foo() # -> 1

# Scope
a_string = "This is a global variable"
def foo():
  print locals()
print globals()
# -> {..., 'a_string': 'This is a global variable'}
foo()
# -> {}

# Variable resolution rules
a_string = "This is a global variable"
def foo():
  print a_string
foo() # -> 'This is a global variable'

a_string = "This is a global variable"
def foo():
  a_string = "test"
  print locals()
foo() # -> {'a_string': 'test'}
a_string # -> 'This is a global variable'

# Variable lifetime
def foo():
  x = 1
foo()
print x # -> NameError: 'x' is not defined

# Function arguments and parameters
def foo(x): # positional parameter
  print locals()
foo(1) # -> {'x': 1}
def foo(x, y=1): # default value parameter
  return x- y
foo(y=1, x=5) # Two named arguments

# Nested functions
def outer():
  x = 1
  def inner():
    print x
  inner()
outer() # -> 1

# Functions are first class object
issubclass(int, object) # all objects in Python inherit from a common baseclass
# -> True
def foo():
  pass
foo.__class__ # -> <type 'function'>
issubclass(foo.__class__, object)
# -> True
# Function as an argument
def add(x, y):
  return x + y
def sub(x, y);
   return x - y
def apply(func, x, y):
  return func(x, y)
apply(add, 1, 2) # -> 3
apply(sub, 2, 1) # -> 1
# Returning a function
def outer():
  def inner():
    print "Inside inner"
  return inner
foo = outer()
foo # -> <function inner at 0x...>
foo() # -> 'Inside inner'

# Closures
# Functions remember their enclosing scope
def outer():
  x = 1
  def inner():
    print x
  return inner
foo = outer()
foo.func_closure # -> {<cell at 0x...; int object at 0x...>}
foo() # -> 1

# Decorators
def outer(some_func):
  def inner(): # replacement function
    print "before some_func"
    ret = some_func()
    return ret + 1
  return inner
def foo():
  return 1
decorated = outer(foo)
decorated()
# -> 'before some_func'
# -> 2
foo = outer(foo) # assigning to a `decorated` foo
# -> <function inner at 0x...>
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __repr__(self):
    return "Coord: " + str(self.__dict__)
def add(a, b):
  return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
  return Coordinate(a.x - b.x, a.y - b.y)
one = Coordinate(100, 200)
two = Coordinate(300, 200)
add(one, two)
# -> Coord: {'y': 400, 'x': 400}
# Bounds checking decorator
def wrapper(func):
  def checker(a, b):
    if a.x < 0 or a.y < 0:
      a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
    if b.x < 0 or b.y < 0:
      b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
    ret = func(a, b)
    if ret.x < 0 or ret.y < 0:
      ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
    return ret
  return checker
one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)
add = wrapper(add)
sub = wrapper(sub)
sub(one, two) # -> Coord: {'y': 0, 'x': 0}
add(one, three) # -> Coord: {'y': 200, 'x': 100}

# The @ symbol applies a decorator to a function
add = wrapper(add)
@wrapper
def add(a, b):
  return Coordinate(a.x + b.x, a.y + b.y)

# *args and **kwargs
def one(*args):
  print args
one(1, 2, 3) # -> 1, 2, 3
lst = [1,2]
add(*lst) # -> 3
def foo(**kwargs):
  print kwargs
foo(x=1, y=2)
# -> {'y': 2, 'x': 1}
dct = {'x': 1, 'y': 2}
def bar(x, y):
  return x + y
bar(**dct) # -> 3

# More generic decorators
def logger(func):
  def inner(*args, **kwargs):
    print "Arguments were: %s, %s" % (args, kwargs)
    return func(*args, **kwargs)
  return inner
@logger
def foo1(x, y=1):
  return x * y
@logger
foo2():
    return 2
foo1(5, 4) 
# -> Arguments were: (5, 4), {}
# -> 20
foo2()
# -> Arguments were: (), {}
2
