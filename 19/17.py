class ListNode():
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def add_two_numbers(l1, l2):
  dummy_head = ListNode()
  carry, current = 0, dummy_head

  while l1 or l2 or carry:
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0

    carry, digit = divmod(val1+val2+carry, 10)

    current.next = ListNode(digit)
    current = current.next

    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

  return dummy_head.next



l1_node1 = ListNode(2)
l1_node2 = ListNode(4)
l1_node3 = ListNode(3)

l1_node1.next = l1_node2
l1_node2.next = l1_node3


l2_node1 = ListNode(5)
l2_node2 = ListNode(6)
l2_node3 = ListNode(4)

l2_node1.next = l2_node2
l2_node2.next = l2_node3


result_head = add_two_numbers(l1_node1, l2_node1)
current_node = result_head
while current_node:
  print(current_node.val, end=' ')
  current_node = current_node.next
print('')