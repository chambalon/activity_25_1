class Person:
  def __init__(self,age):
    if age<0:
      print("Age is not valid, setting age to 0.")
      self.age = 0
    else:
      self.age = initialAge

  def amIOld(self):
    if self.age<13:
      print("you're young")
    elif self.age>=13 and self.age<18:
      print("you're a teenager")
    else:
      print("You're old")

  def yearPasses(self):
    self.age += 1



if __name__ == '__main__':
  testCases = int(input())
  for i in range(0,testCases):
    initialAge = int(input())
    p = Person(initialAge)
    p.amIOld()
    for j in range(0,3):
      p.yearPasses()
    p.amIOld()
    print("")