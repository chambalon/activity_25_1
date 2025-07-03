'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
  alist = []
  for i in range(int(input("enter n: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    alist.append([name,score])
print(alist)
#alist1 = set([score for name, score in alist])

alist1 = sorted(set([score for name, score in alist]))    # score is the output
second_lowest = alist1[1]
print(alist1)
print(second_lowest)
#‘\n’.join will print the names in different lines
print("\n".join([name for name, score in alist if score == second_lowest]))     # name is the output





