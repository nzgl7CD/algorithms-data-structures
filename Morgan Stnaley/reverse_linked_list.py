def reverse_linked_list(head):
    if not head or not head.next:return head
    rest=reverse_linked_list(head.next)
    
    head.next.next=head
    head.next=None
    
    return rest
    