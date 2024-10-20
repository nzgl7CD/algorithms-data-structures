'''
- The root node of the subtree is visited first.
- Then the left subtree  is traversed.
- At last, the right subtree is traversed.

'''

class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print preorder traversal
def printPreorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)

    # Recur on right subtree
    printPreorder(node.right)


# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    
    '''
    
     1
    / \
   2   3
  / \   \ 
4    5   6

    '''

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreorder(root)