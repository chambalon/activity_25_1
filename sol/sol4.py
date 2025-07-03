# Find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
  n = int(input("enter no.of. scores n: "))
  arr = list(map(int,input("Enter n number of scores (in the same line)").split()))
  # convert list to set so, it will not store multiple same integers.
  arr2 = set(arr)
  #print(arr2)
  arr_sorted = sorted(arr2)
  print(arr_sorted[-2])



  
 