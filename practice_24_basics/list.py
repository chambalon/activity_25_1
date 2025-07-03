l1= [1,2,3,4,5]
print("list:",l1)
print("****************************")

print("first element:",l1[0])
print("last element:",l1[-1])
print("lasst element:",l1[len(l1)-1])
print("****************************")

l1[2] = "Three"
print("modified list:",l1)
del(l1[4])
print("newlist:",l1)
print("****************************")

# Add new elements to a list: append() – At the end. insert() - Wherever we like .
l1.append(100)
print("appended 100 to the list",l1)
l1.insert(3,"four")
print("inserted \'four' at 3rd index:",l1)
print("****************************")

l2=l1+[200]
print("list2:",l2)
l3=[]
l4=l3+[300]
print("list4:",l4)
print("****************************")

# slicing operator list[start:stop:step] stop should be last index+1 to include the last element 
mylist= [11,22,33,44,55]
print("whole list:",mylist[0:5:1])
print("whole list:",mylist[::])
print(mylist[::2])
print(mylist[1:4:2])
print("reversed list",mylist[::-1])
print("****************************")
# in and not in -> returns boolean
print(33 in mylist)
print(1000 in mylist)
print("****************************")

li=[2,3,8]
li.insert(0,1)
print(li)

