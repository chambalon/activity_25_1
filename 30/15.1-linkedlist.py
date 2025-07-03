# insert_at_begining

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Linkedlist:
  def __init__(self):
    self.head = None

  def insert_at_begining(self,data):
    new_node = Node(data)
    new_node.next = self.head     # points to the old head
    self.head = new_node

  def traverse_and_print(self):
    current_node = self.head
    while current_node:
      print(current_node.data, end="->")
      current_node = current_node.next
      return



linked_list = Linkedlist()


linked_list.insert_at_begining(3)

linked_list.traverse_and_print()
