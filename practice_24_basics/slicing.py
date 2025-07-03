# slicing operator list[start:stop:step] stop should be last index+1 to include the last element 
# Slicing creates a new list
# Can be used to reverse a list

mylist= [11,22,33,44,55]
print("whole list:",mylist[0:5:1])
print("whole list:",mylist[::])
print(mylist[::2])
print(mylist[1:4:2])

# reverse a list
print("reversed list",mylist[::-1])
print("****************************")

list1= [100,101,102]
list2= list1
list2.append(103)
print("list1:",list1)
print("list2:",list2)   # list1 has also changed

# using slicing, first list will remain the same as a new list is created
list3= [100,101,102]
list4= list3[::]
list4.append(103)
print("list3:",list3)
print("list4:",list4)
