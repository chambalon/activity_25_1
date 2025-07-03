
#from abc import ABC, abstractmethod

#class AdvancedArithmetic(ABC):
  #@abstractmethod
  #def divisorSum(n):



class AdvancedArithmetic(object):
  def divisorSum(n):
    raise NotImplementedError
  
class Calculator(AdvancedArithmetic):
  def divisorSum(self,n):
    sum = 0
    for i in range(1,n+1):
      if n%i == 0:
        sum += i
    return sum
  
n= int(input())
cal = Calculator()
result = cal.divisorSum(n)

print(f'I Implemented: {type(cal).__bases__[0].__name__}')
print(result)