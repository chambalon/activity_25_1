import heapq

class ListNode():
  def __init__ (self,val=0, next=None):
    self.val = val
    self.next =next

def mergeKLists(lists):
  min_heap = []
  dummy_head = ListNode()
  current = dummy_head

  for i, node in enumerate(lists):
    if node:
      heapq.heappush(min_heap, (node.val,i,node))

  while min_heap:
    val, idx, node = heapq.heappop(min_heap)
    current.next = node
    current = current.next

    if node.next:
      heapq.heappush(min_heap, (node.next.val,idx,node.next))
  
  return dummy_head.next


l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))

lists = [l1,l2,l3]

mergedlist_head = mergeKLists(lists)
current_node = mergedlist_head

result = []
while current_node:
  result.append(current_node.val)
  current_node = current_node.next
print(result)
  