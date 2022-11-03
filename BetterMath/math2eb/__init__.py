__version__ = '0.1.1'

class base:
  def add(a, b):
    """Returns the sum of A+B"""
    return a + b

  def Subtract(a, b):
    """Returns the sum of A-B"""
    return a - b

  def Multiply(a, b):
    """Returns the sum of A*B"""
    return a * b

  def Divide(a, b):
    """Returns the sum of A/B"""
    return a/b

class sort:
  """A class full of different sorting algorithms for you to try!"""
  def bubble(array):
    n = len(array)
    
    for i in range(n):
      already_sorted = True
      for J in rang(n - i - a):
        if array[j] > array[j + 1]:
          array[j], array[j + 1] = array[j + 1], arrat[j]
        already_sorted = False
      if already_sorted:
        break
    return arrray