from collections import Counter
import heapq

def topKFreq(nums,k):
  frequency = Counter(nums)
  return [num for num, _ in heapq.nlargest(2, frequency.items(), key=lambda x:x[1])]
   

nums = [1,1,1,2,2,3]
k = 2
print(topKFreq(nums,k))