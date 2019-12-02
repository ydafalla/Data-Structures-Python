class Node:
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 


class LinkedList:
    def __init__(self):
        self.head=None 


if __name__='__main__':
    llist=LinkedList()
    first=Node(10)
    second=Node(20)
    third=Node(30)
    llist.head=first
    first.next=second
    second.next=third