# A simple matrix class that does operations: add, sub, mult, and div
# Only allows integers
# Notes
# - To multiply a matrix by a scalar (integer), use MatrixObj * 2, not 2 * MatrixObj
class Matrix:
  def __init__(self, dimension1 = None, dimension2 = None):
    if dimension1 is None and dimension2 is None:
      self.matrix = None

    elif type(dimension1) is int and dimension2 is None:
      self.matrix = []

      for i in range(dimension1):
        tempArr = []
        for o in range(dimension1):
          tempArr.append(0)
        self.matrix.append(tempArr)

    elif type(dimension1) is int and type(dimension2) is int:
      self.matrix = []

      for i in range(dimension1):
        tempArr = []
        for o in range(dimension2):
          tempArr.append(0)
        self.matrix.append(tempArr)

    else:
      return None

  # Add operation, + overloaded
  def __add__(self, otherMatrix):
    if self.matrix is None or otherMatrix.matrix is None:
      print("Empty matrices detected")
      return None

    if len(self.matrix) == len(otherMatrix.matrix) and len(self.matrix[0]) == len(otherMatrix.matrix[0]):
      returnMatrix = Matrix(len(self.matrix), len(self.matrix[0]))

      for i in range(len(returnMatrix.matrix)):
        for o in range(len(returnMatrix.matrix[i])):
          returnMatrix.matrix[i][o] = self.matrix[i][o] + otherMatrix.matrix[i][o]

      return returnMatrix
    else:
      print("Different dimensions on matrices")
      return None

  # Subtract operator, - overloaded
  def __sub__(self, otherMatrix):
    if self.matrix is None or otherMatrix.matrix is None:
      print("Empty matrices detected")
      return None

    if len(self.matrix) == len(otherMatrix.matrix) and len(self.matrix[0]) == len(otherMatrix.matrix[0]):
      returnMatrix = Matrix(len(self.matrix), len(self.matrix[0]))

      for i in range(len(returnMatrix.matrix)):
        for o in range(len(returnMatrix.matrix[i])):
          returnMatrix.matrix[i][o] = self.matrix[i][o] - otherMatrix.matrix[i][o]

      return returnMatrix
    else:
      print("Different dimensions on matrices")
      return None

  # Multiplication operator, * overloaded
  def __mul__(self, otherData):
    if self.matrix is None:
      return 0

    # Matrix * Integer
    if type(otherData) is int:
      returnMatrix = Matrix(len(self.matrix), len(self.matrix[0]))

      for i in range(len(returnMatrix.matrix)):
        for o in range(len(returnMatrix.matrix[i])):
          returnMatrix.matrix[i][o] = otherData * self.matrix[i][o]

      return returnMatrix

    # Matrix * Matrix
    if type(otherData) is Matrix and otherData.matrix is not None:
      # Matrix compatability
      if len(self.matrix[0]) == len(otherData.matrix):
        returnMatrix = Matrix(len(self.matrix), len(otherData.matrix[0]))

        # These 2 nested for loops dictate which
        # index of returnMatrix we're placing in
        for i in range(len(self.matrix)):
          for o in range(len(otherData.matrix[0])):
            for p in range(len(otherData.matrix)):
              returnMatrix.matrix[i][o] += self.matrix[i][p] * otherData.matrix[p][o]

        return returnMatrix

    return None

  # Sets values from the user into the matrix
  def read(self):
    if self.matrix is None:
      print("Empty matrix")
      return

    for i in range(len(self.matrix)):
      for o in range(len(self.matrix[i])):
        print("Enter value for self.matrix[", i, "][", o, "]: ", end = '')
        inp = int(input())
        self.matrix[i][o] = inp

  def print(self):
    if self.matrix is None:
      print("Empty matrix")
      return

    for i in range(len(self.matrix)):
      for o in range(len(self.matrix[i])):
        print(self.matrix[i][o], end = '')
        if o != (len(self.matrix[i]) - 1):
          print(", ", end = '')
      print()
