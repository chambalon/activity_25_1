"""
The scope of the array and integer is the entire class instance. 
The class constructor saves the argument passed to the constructor as the instance variable 
(where the computeDifference method can access it).
"""

class Difference:
  def __init__(self,arr):
    self.__elements = arr
    self.max_diff = 0

  def compute_diff(self):
    max_value = 0
    min_value = 101
    for element in self.__elements:
      if element > max_value:
        max_value = element
      if element < min_value:
        min_value = element
    self.max_diff = max_value - min_value


_ = input()
arr = [int(e) for e in input().split()]   # list(map(int,input().split()))

d = Difference(arr)
d.compute_diff()
print(d.max_diff)

