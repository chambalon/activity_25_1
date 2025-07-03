def func1():
    print("Pyhton is awesome")
func1()


def func2():
    x= 'Python'
    y= 'Java'
    z= 'C'
    # variables returned as tuple
    return x,y,z
    # variables returned as 
    #return [x,y,z]
    # return none
    #return
print(func2())
# method 2
#output=func2()
#print(output)

print("***************************************")

def func3(parameter1,parameter2):
    x= parameter1+parameter2
    return x
print(func3('ardument1','argument2'))