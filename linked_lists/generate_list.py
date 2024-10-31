class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    # Add to the back
    def append(self, data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node
        
    #Add to the front
    def prepend(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def delete(self, data):
        if not self.head:
            return
            
        if self.head.data == data:
            self.head = self.head.next
            return
            
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

# Example usage
if __name__ == "__main__":
    # Create a new linked list
    llist = LinkedList()
    
    # Add some elements
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.prepend(0)
    
    # Display the list: 0 -> 1 -> 2 -> 3
    print(llist.display())
    
    # Delete an element
    llist.delete(2)
    
    # Display the updated list: 0 -> 1 -> 3
    print(llist.display())