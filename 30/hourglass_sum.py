def max_hourglass_sum(arr):

  row = len(arr)
  col = len(arr[0])
  max_sum = float('-inf') # max_sum = -63

  for i in range(row-2):
    for j in range(col-2):
      sum  = ( arr[i][j]+arr[i][j+1]+arr[i][j+2]+
              arr[i+1][j+1]+
              arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
      )
      max_sum = max(max_sum,sum)

  return max_sum


matrix1 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

result = max_hourglass_sum(matrix1)
print(result)