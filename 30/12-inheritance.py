# Observe that Student inherits all the properties of Person.

class Person:
  def __init__(self,firstname,lastname,id):
    self.firstname = firstname
    self.lastname = lastname
    self.id = id
  def print_person(self):
    print(f'Name: {firstname} {lastname}')
    print(f'ID: {id}')
  
class Student(Person):
  def __init__(self,firstname,lastname,id,scores):
    self.scores = scores
    Person.__init__(self,firstname,lastname,id)

  def calculate(self):
    sum = 0
    for score in scores:
      sum +=score

    average = sum/len(scores)

    if average < 80:
      return 'C'
    elif average < 90:
      return 'B'
    else:
      return 'A'
    

entry = input().split()
firstname = entry[0]
lastname = entry[1]
id =entry[2]

scores = list(map(int, input().split()))

s = Student(firstname,lastname,id,scores)
s.print_person()
grade = s.calculate()
print(f"grade: {grade}")
    









