'''
A linked list is a linear data structure that stores data in nodes, which are connected by pointers. Unlike arrays, 
linked lists are not stored in contiguous memory locations.

- Dynamic: Linked lists can be easily resized by adding or removing nodes.

- Non-contiguous: Nodes are stored in random memory locations and connected by pointers. 
(elements are spread out in different locations in memory rather than being in a continuous block, meaning non constant access)

- Sequential access: Nodes can only be accessed sequentially, starting from the head of the list.

'''

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def get_head(self):
        return self.head
    
    def insert_node(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    
    def delete_nodes(self,key):
        current_node=self.head
        previous=None
        while current_node and current_node.data!=key:
            previous=current_node
            current_node=current_node.next
        if current_node is None:
            return
        if previous is None:
            self.head=current_node.next
        else:
            previous.next=current_node.next
    
    def search_linked_list(head, target):
        # Traverse the Linked List
        while head is not None:
            # Check if the current node's data matches the target value
            if head.data == target:
                return True  # Value found
            # Move to the next node
            head = head.next
        return False 
    
    def display(self, head):
        current_node=head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node=current_node.next
        print('None')


            