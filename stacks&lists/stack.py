'''
- A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
- This means the last element added to the stack is the first one to be removed. 
- Think of a stack of plates—if you add plates to the top, you can only remove the top plate first.
'''
stack = []

# Pushing elements onto the stack (push operation)
stack.append(1)
stack.append(2)
stack.append(3)


# Popping elements from the stack (pop operation)
stack.pop()

# Checking the top element of the stack (peek)
stack[-1]