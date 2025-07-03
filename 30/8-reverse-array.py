def revArr(arr1,n):
  for j in range(0,n//2):
    temp = arr1[j]
    arr1[j] = arr1[n-1-j]
    arr1[n-1-j] = temp
  print(" ".join(arr1))


if __name__ == '__main__':
  n = int(input())
  arr1 = input(f"enter {n} integers separated by space:").split()
  #arr2 = list(map(int,input().split()))
  print(arr1)
  revArr(arr1,n)