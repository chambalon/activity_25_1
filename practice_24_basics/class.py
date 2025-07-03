class Person():
    def __init__(self,name,age,profesion):
        self.name= name
        self.age= age
        self.profesion= profesion

    def printInfo(self):
        print("My name is",self.name, "I am",self.age, "I work as a",self.profesion)


p1= Person('Crystal',28,'Developer')
p2= Person('Hannah',28,'Programer')
p1.printInfo()
p2.printInfo()

