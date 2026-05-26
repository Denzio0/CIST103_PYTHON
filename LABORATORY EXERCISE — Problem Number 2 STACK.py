#MARC RODEN D. FAMERO
#DATA STRUCTURES AND ALGORITHM - DSA (CIST103)
#LABORATORY EXERCISE — Problem Number 1 - STACK

# Stack using one-dimensional array
stack = []

def push(item):
    stack.append(item)

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Popped:", stack.pop())

def display_stack():
    print("Stack elements:", stack)

# Stack operations
push(10)
push(20)
push(30)
display_stack()
pop()
display_stack()
