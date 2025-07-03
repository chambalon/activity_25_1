# bubble sort
  
if __name__ == '__main__':

  n = int(input())
  arr = [int(e) for e in input().split()]

  total_swap_count = 0
  for i in range(n):
    swap_count = 0
    for j in range(n-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1],arr[j]
        swap_count += 1
    total_swap_count += swap_count

    if swap_count == 0 :
      break

  print(f'Array is sorted in {total_swap_count} swaps')
  print(f'First element: {arr[0]}')
  print(f'Last element: {arr[n-1]}')
