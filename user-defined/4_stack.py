def create_stack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    print("pushed , ", item)

def check_empty(stack):
    return len(stack) == 0

def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"
    else:
        stack.pop()

stack = create_stack()
push(stack, 6)
push(stack, 9)
print(stack)
pop(stack)
print(stack)
push(stack, 10)
#print(stack.peek())