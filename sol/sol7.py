'''
Consider a list (list = []). You can perform the following commands:

insert i, e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':

  alist = []
  n = int(input("n : "))
  
  for i in range(n):
    # split() splits the string input into a list of strings. 
    command = input("Enter your command: ").split()
    if command[0] == "insert" :
      alist.insert(int(command[1]),int(command[2]))
    
    elif command[0] == "print":
      print(alist)

    elif command[0] == "remove" :
      alist.remove(int(command[1]))

    elif command[0] == "append" :
      alist.append(int(command[1]))
    
    elif command[0] == "sort" :
      alist.sort()
    
    elif command[0] == "pop" :
      alist.pop()

    elif command[0] == "reverse" :
      alist.reverse()
    else:
      print("Invalid command!")
      

 


  


