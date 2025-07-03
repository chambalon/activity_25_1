# tuple can be created in two ways

# Method 1
mytuple1= (1,2,3,4)

print("mytuple1:",mytuple1)
print("type of mytuple1 is:",type(mytuple1))

# Method 2
mytuple2= 1,2,3

print("mytuple2:",mytuple2)
print("type of mytuple2 is:",type(mytuple2))

print("********************************************")

emptytuple=()
print("empty tuple: ",emptytuple)

single_tuple= (5)
print("single item tuple: ",single_tuple)

mixed_tuple= (3, "hello", "python", 9)
print("mixed tuple: ",mixed_tuple)

print("********************************************")
# duplicats allowed
t=(1,7,7)
print(t)
print("********************************************")


t1 =(1,2,3)
t2=('hi',6,2)
t3= (2)
print("add two tuples:", t1+t2)
print("multiply t1,t3:",t3*t1)

print("length of t1:",len(t1))
# in or not in - tuple
print("is 2 in t2:", 2 in t2)




