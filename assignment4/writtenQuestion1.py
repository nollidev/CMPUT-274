def push_with_priority(stack, priority, element):
    # Temporary stack to hold elements until right position is found
    temp_stack = []
    
    # 1) Move elements to temp_stack while maintaining priority order
    while True:
        if len(stack) < 1: break
        elif stack[-1][0] > priority: break 
        else: temp_stack.append(stack.pop())

    # 2) Insert the new element with its priority
    stack.append((priority, element))

    # 3) Move the elements back from temp_stack to stack to maintain their order
    while len(temp_stack) > 0: stack.append(temp_stack.pop())
    
    return stack

# Example usage
stack = []
push_with_priority(stack, 3, "A")
push_with_priority(stack, 1, "B")
push_with_priority(stack, 2, "C")
print(stack)