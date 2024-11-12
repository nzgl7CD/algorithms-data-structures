class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def insert(self, data):
        new_node=Node(data)
        if not self.head: self.head=new_node; return
        
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
            print(current_node.data)
        current_node.next=new_node
    
    def display(self):
        if not self.head: return
        elements=[]
        current=self.head
        while current:
            elements.append(str(current.data))
            current=current.next
        return ' -> '.join(elements)

if __name__ == "__main__":
    # Create a new linked list
    llist = LinkedList()
    
    # Add some elements
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    
    print(llist.display())