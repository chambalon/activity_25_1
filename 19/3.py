# Median of Two Sorted Arrays
# When you have two sorted arrays, you need to find the median of the combined elements as if they were in a single sorted array.

def median_sorted_arrays(nums1,nums2):
  nums = sorted(nums1+nums2)
  n = len(nums)
  print(nums)
  if n%2 == 0:
    return (nums[n//2-1]+nums[n//2])/2
  else:
    return nums[n//2]
  
  
nums1 = [2,1,5,8]
nums2 = [7,3,2,6,1,4]

result = median_sorted_arrays(nums1,nums2)
print(result)