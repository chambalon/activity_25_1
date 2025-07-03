print("string1")
print('string2\"')
print("strring3\\")
# When creating a multi-line string. Any unescaped quotes or newline characters are retained, except those used to enclose the string.  
print("""this   
is " '
string4""")
print("2345")

print('*******************************')

"""
this 
is 
multiline
comment
"""
print('*******************************')
print(7/3)
# Floor division.  
print(7//3)
# Exponent (Powers). 
print(10 ** 3)
print('*******************************')
a=3
b=6
print(a>b)
print(a<b)
print(a>=1 or b<3)
print(a>=3 and b==6)
print('*******************************')

mark = int(input("Eter your mark: \n"))
if mark >= 50:
    if mark > 80:
        print("Congratulations on your achievement\n")
    else:
        print("Congratulations! you have passed\n")
else:
    print("Unfortunately you have failed\n")
print('*******************************')

numsequence = [1,2,3,4,5]
for num in numsequence:
    print(num)
print('*******************************')

for n in range(10):
    print(n)
print('*******************************')

for n in range(1,11):
    print(n)
print('*******************************')

for n in range(0,20,3):
    print(n)
print('*******************************')

for n in range(6):
    if n == 3:
        continue
    print(n)
print('*******************************')

for n in range(6):
    if n == 3:
        break
    print(n)
print('*******************************')

for n in range(6):
    if n == 3:
        pass
    print(n)
print('*******************************')