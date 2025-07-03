#The provided code stub is read in a dictionary containing key/value pairs of name:[Marks] for a list of students. 
# Print the average of the marks array for the student name is provided, showing 2 places after the decimal.

if __name__ == '__main__':
  n = int(input("n: "))
  student_Records = {}

  for i in range(n):
    name, *marks = input("name and marks: ").split()
    scores = list(map(float, marks))
    student_Records[name] = scores

  print(student_Records)
  print(scores)

  query_name = input("name: ")
  list1 =student_Records[query_name]

  print(list1)

  average = sum(list1)/len(list1)
  print("%.2f" % average)