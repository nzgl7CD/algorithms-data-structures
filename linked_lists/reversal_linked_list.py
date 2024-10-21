from generate_list import LinkedList 

ll = LinkedList()

# Add nodes to the linked list
ll.insert_node(10)
ll.insert_node(20)
ll.insert_node(30)

ll.display(ll.get_head())  # Output: 10 -> 20 -> 30 -> None

def reverse_list(head):
    if head is None or head.next is None:
        return head
    remaining=reverse_list(head.next)
    head.next.next=head
    head.next=None
    return remaining

reversed_list=reverse_list(ll.get_head())
ll.display(reversed_list) # Output: 30 -> 20 -> 10 -> None






    