from Matrix import *

if __name__ == "__main__":
  obj1 = Matrix(2, 2)
  obj1.read()
  print()

  obj2 = Matrix(2, 2)
  obj2.read()
  print()

  obj3 = obj1 + obj2
  obj3.print()
  print()

  obj3 = obj1 - obj2
  obj3.print()
  print()

  obj3 = obj1 * obj2
  obj3.print()
