class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list
    
    def delete(self, key):
        current = self.head
        previous = None
        while current and current.data != key:  # Find the node to delete
            previous = current
            current = current.next
        
        if current is None:  # The key was not found
            return
        
        if previous is None:  # The node to delete is the head
            self.head = current.next
        else:
            previous.next = current.next  # Bypass the node to delete


linked_list = LinkedList()
linked_list.append(10) # -> O(1)
linked_list.append(20) # -> O(n)
linked_list.append(30)
linked_list.display() #-> No random access: -> O(n)

