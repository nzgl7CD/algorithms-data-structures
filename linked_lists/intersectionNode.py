def getIntersactionNode(head1, head2):
    if not head1 and not head2: return None
    ptr1,ptr2=head1,head2
    while ptr1!=ptr2:
        ptr1=ptr1.next if ptr1 else head2
        ptr2=ptr2.next if ptr2 else head1
    return ptr1
