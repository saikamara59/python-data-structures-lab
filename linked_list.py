class Node:
    """"
    "An object for storing a single node a linked list."
    "Models two attritubutes - data and the lnik to the next node in the list
    """

    data = None
    next_node = None 

    def __init__(self,data):
        self.data = data


    def __repr__(self):
      return "<Node data: %s>" % self.data
    
class LinkedList:
#   Singly Linked List

   def __init__(self):
      self.head = None   

   def is_empty(self):
      return self.head == None
   
   def size(self):
    #  Returns the number of nodes in the list Takes 0(n) time
     current = self.head
     count = 0

     while current:
        count += 1
        current = current.next_node

     return count 
   



   def add(self,data):
   # Adds a new node containing data at the head of the list Takes 0(1) time.
     new_node = Node(data)
     new_node.next_node = self.head
     self.head = new_node