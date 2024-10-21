# Post Order traversal 
# of Binary Tree in O(N) 
# time and O(1) space 
class node:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None


def newNode(data):

    temp = node(data)
    return temp

def postOrderConstSpace(root):

    if (root == None):
        return

    current = newNode(-1)
    pre = None
    prev = None
    succ = None 
    temp = None 
    
    current.left = root
        
    while (current):

        if (current.left == None):
            current = current.right
        else:
            pre = current.left

            while (pre.right and 
                   pre.right != current):
                pre = pre.right

            if (pre.right == None): 
                
                # Make current as the right 
                # child of the right most node 
                pre.right = current 
                current = current.left
            
            else:
            
                pre.right = None
                succ = current
                current = current.left 
                prev = None

                while (current != None): 
                    temp = current.right
                    current.right = prev 
                    prev = current
                    current = temp 

                while (prev != None): 
                    print(prev.data, end = ' ')
                    temp = prev.right
                    prev.right = current
                    current = prev
                    prev = temp

                current = succ
                current = current.right 

# Driver code 
if __name__=='__main__':
    
    ''' Constructed tree is as follows:- 
                       1 
                    /     \ 
                   2      3 
                  / \     / \ 
                 4   5  6   7 
                    / \ 
                   8   9 
        '''
    root = None 

    root = newNode(1)
    root.left = newNode(2) 
    root.right = newNode(3) 

    root.left.left = newNode(4) 
    root.left.right = newNode(5) 

    root.right.left = newNode(6) 
    root.right.right = newNode(7)

    root.left.right.left = newNode(8) 
    root.left.right.right = newNode(9) 
    
    postOrderConstSpace(root)

