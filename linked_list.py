# class Node:
#     """"
#     "An object for storing a single node a linked list."
#     "Models two attritubutes - data and the lnik to the next node in the list
#     """

#     data = None
#     next_node = None 

#     def __init__(self,data):
#         self.data = data


#     def __repr__(self):
#       return "<Node data: %s>" % self.data
    
# class LinkedList:
# #   Singly Linked List

#    def __init__(self):
#       self.head = None   

#    def is_empty(self):
#       return self.head == None
   
#    def size(self):
#     #  Returns the number of nodes in the list Takes 0(n) time
#      current = self.head
#      count = 0

#      while current:
#         count += 1
#         current = current.next_node

#      return count 
   



#    def add(self,data):
#    # Adds a new node containing data at the head of the list Takes 0(1) time.
#      new_node = Node(data)
#      new_node.next_node = self.head
#      self.head = new_node

class node:
    def __init__(self, data=None):
        self.data = data      # Correct: Assign the data passed in
        self.next = None      # Add next pointer

class linked_list:
    def __init__(self):
        self.head = node()  # Dummy node to simplify appending

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

# Test the list
my_list = linked_list()
my_list.append(3)
my_list.append(5)

my_list.display()  # Output: [3, 5]
