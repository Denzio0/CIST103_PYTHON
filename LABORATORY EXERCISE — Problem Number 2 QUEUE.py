#MARC RODEN D. FAMERO
#DATA STRUCTURES AND ALGORITHM - DSA (CIST103)
#LABORATORY EXERCISE — Problem Number 2 - QUEUE

# Queue using one-dimensional array
queue = []

def enqueue(item):
    queue.append(item)

def dequeue():
    if not queue:
        print("Queue Underflow")
    else:
        print("Dequeued:", queue.pop(0))

def display_queue():
    print("Queue elements:", queue)

# Queue operations
enqueue(5)
enqueue(15)
enqueue(25)
display_queue()
dequeue()
display_queue()
