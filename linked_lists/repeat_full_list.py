class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        
    def append(self,data):
        new_node=Node(data)
        if not self.head: self.head=new_node; return
        
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        return