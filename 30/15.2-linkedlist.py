# insert_at_end

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Linkedlist:
  def __init__(self):
    self.head = None

  def insert_at_end(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node
    
    
  def traverse_and_print(self):
    current_node = self.head
    while current_node:
      print(current_node.data, end="->")
      current_node = current_node.next
  


linked_list = Linkedlist()

for i in range(1,6):
  linked_list.insert_at_end(i)

linked_list.traverse_and_print()