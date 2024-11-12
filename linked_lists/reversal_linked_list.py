from generate_list import LinkedList 

ll = LinkedList()

# Add nodes to the linked list
ll.append(10)
ll.append(20)
ll.append(30)


def reverse_list(head):
    if head is None or head.next is None:
        return head
    remaining=reverse_list(head.next)
    head.next.next=head
    head.next=None
    return remaining

reversed_list=reverse_list(ll.get_head())

elements=[]
current=reverse_list
while current:
    elements.append(str(current.data))
    current=current.next
print(''.join(elements))






    