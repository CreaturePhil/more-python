class Vector:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getX(self):
    return self.x

  def getY(self):
    return self.y

v = Vector(1, 2)
print v.getX(), v.getY()
