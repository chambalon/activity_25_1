if __name__ == '__main__':
  n = int(input())
  arr = list(map(int,input().rstrip().split()))
  print(arr)

  revArr = []
  for i in range(n):
    revArr.append(arr[n-1-i])
  
  print(" ".join(str(e) for e in revArr))

  # second print method

  revString = ''
  for i in range(len(revArr)):
    revString += str(revArr[i]) + ' '
  print(revString)
 
  