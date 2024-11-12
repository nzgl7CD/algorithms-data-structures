
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if not self.head: self.head=new_node; return
        current_node=self.head #head -> [1 | next] -> [2 | next] -> [3 | next] -> [4 | NULL] -> NONE (Data|Next)
        while current_node.next: #stops at the last node with a value, [4 | NULL]
            current_node=current_node.next
        current_node.next=new_node
    
    def delete(self, data):
        if not self.head: return
        if self.head.data==data: self.head=self.head.next; return #self.head.data=1
        current=self.head
        while current.next:
            if current.next.data==data: current.next=current.next.next; return
            current=current.next
    
    def display(self):
        if not self.head: return None
        elements=[]
        current_node=self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node=current_node.next
        print(' -> '.join(elements))
    
    def return_head(self):
        return self.head
        
def reverse(head):
    if head is None or head.next is None: return head
    rest=reverse(head.next)
    head.next.next=head
    head.next=None
    return rest

def doubleReverse(head):
    if head is None or head.next is None:
        return head
    
    curr = head
    while curr:
        # Swap the next and prev pointers for each node
        curr.prev, curr.next = curr.next, curr.prev
        curr = curr.prev  # Move to the next node (which is actually the previous node after swapping)

    # The new head will be the last node after reversal
    return head.prev

def displayRev(head):
    if not head: return 
    elements=[]
    curr=head
    while curr:
        elements.append(str(curr.data))
        curr=curr.next
    return ' -> '.join(elements)

def intersectionNode(head1, head2):
    if not head1 and not head2: return None
    ptr1,ptr2=head1,head2
    while ptr1!=ptr2:
        ptr1=ptr1.next if ptr1 else head2
        ptr2=ptr2.next if ptr2 else head1
    return ptr1
    
    
    
llObj=LinkedList()
llObj.append(1)
llObj.append(2)
llObj.append(3)
llObj.append(4)
llObj.append(5)
llObj.display()

llObj1=LinkedList()
llObj1.append(2)
llObj1.append(3)
llObj1.append(4)
llObj1.append(5)
llObj1.append(6)
llObj1.display()

head=llObj.return_head()

head1=llObj1.return_head()
reversedHead=reverse(head1)
print(displayRev(reversedHead))


# dblReversed=doubleReverse(head1)
# print(displayRev(dblReversed))





            
            
        
        