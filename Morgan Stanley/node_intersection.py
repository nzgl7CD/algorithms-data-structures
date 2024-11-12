def getIntersectionNode(headA, headB):
    if not headA or not headB: return None
    ptr1,ptr2=headA,headB
    while ptr1!=ptr2:
        ptr1=ptr1.next if ptr1 else headB
        ptr2=ptr2.next if ptr2 else headA
    return ptr1