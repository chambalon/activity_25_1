'''
List comprehension! 
You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. 
Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Use list comprehensions rather than multiple loops.
'''

if __name__ == '__main__':
  # Four integers x, y, z and n, each on a separate line.
  x = int(input("enter x:"))
  y = int(input("enter y:"))
  z = int(input("enter z:"))
  n = int(input("enter n:"))

  print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n))
