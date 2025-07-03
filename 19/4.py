# Search for a target in Rotated Sorted Array

def search_rotated_sorted(nums,target):
  left, right = 0, len(nums)-1

  while left<=right:
    mid = (left+right)//2
    if nums[mid] == target:
      return mid
    if nums[left] <= nums[mid]:
      if nums[left]<=target<nums[mid]:
        right = mid-1
      else:
        left = mid+1
    else:
      if nums[mid]<target<=nums[right]:
        left = mid+1
      else:
        right = mid-1
  return -1


nums = [5,6,7,1,2,3,4]
target = 7

result = search_rotated_sorted(nums,target)
print(result)