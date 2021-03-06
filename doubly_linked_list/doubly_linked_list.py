"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
      node_to_add = ListNode(value)
      if self.head is None:
          self.head = node_to_add
      else:
          self.head.insert_before(value)
          self.head = node_to_add
          
  def remove_from_head(self):
      if self.head is None:
          return None
      elif self.head is not None:
          head_to_delete = self.head
          if self.head.next is not None:
              self.head.delete()
              self.head = self.head.next
              return head_to_delete.value


  def add_to_tail(self, value):
      node_to_add = ListNode(value)
      if self.tail is None:
          self.tail = node_to_add
      elif self.tail is not None:
          self.tail.insert_after(value)
          self.tail = node_to_add
      

  def remove_from_tail(self):
      if self.tail is not None:
          temp = self.tail
          self.tail.delete()
          return temp

  def move_to_front(self, node):
      current_node = self.head
      while current_node is not None:
          if current_node == node:
              self.add_to_head(node.value)
              node.delete()
          current_node = current_node.next

  def move_to_end(self, node):
      current_node = self.head
      while current_node is not None:
          if current_node == node:
              self.add_to_tail(node.value)
              node.delete()
          current_node = current_node.next

  def delete(self, node):
      temp = node
      node.delete()
      return temp.value
    
  def get_max(self):
      current_node = self.head
      max = 0
      while current_node is not None:
          if current_node.value > max:
              max = current_node.value
              current_node = current_node.next
          return max

 
