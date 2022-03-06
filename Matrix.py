class Matrix:
  def __init__(self, d1 = None, d2 = None):
    # Empty matrix
    if d1 == None and d2 == None:
      self.matrix = None

    # n x n
    elif d1 != None and d2 == None:
      if type(d1) is int:
        self.matrix = []

        # What we're adding to self.matrix
        tempArr = []
        for i in range(d1):
          tempArr.append(0)
        for i in range(d1):
          self.matrix.append(tempArr)
            
    # n x m
    else:
      if type(d1) is int and type(d2) is int:
        self.matrix = []
        tempArr = []

        for i in range(d1):
          tempArr.append(0)
        for o in range(d2):
          self.matrix.append(tempArr)

  def print(self):
    if self.matrix is None:
      print("Empty matrix")
      return

    for i in range(len(self.matrix)):
      for o in range(len(self.matrix[i])):
        print(self.matrix[i][o], end = '')
        
        if o != (len(self.matrix[i]) - 1):
          print(",", end = ' ')
      print()

