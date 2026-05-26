#MARC RODEN D. FAMERO
#DATA STRUCTURES AND ALGORITHM - DSA (CIST103)
#LABORATORY EXERCISE — Problem Number 2 - CIRCULAR QUEUE

# Circular Queue using array
size = 5
cqueue = [None] * size
front = -1
rear = -1

def enqueue_cq(item):
    global front, rear
    if (rear + 1) % size == front:
        print("Circular Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear = (rear + 1) % size
        cqueue[rear] = item

def dequeue_cq():
    global front, rear
    if front == -1:
        print("Circular Queue Underflow")
    else:
        print("Dequeued:", cqueue[front])
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size

def display_cq():
    if front == -1:
        print("Circular Queue is empty")
    else:
        i = front
        print("Circular Queue elements:", end=" ")
        while True:
            print(cqueue[i], end=" ")
            if i == rear:
                break
            i = (i + 1) % size
        print()

# Circular Queue operations
enqueue_cq(1)
enqueue_cq(2)
enqueue_cq(3)
display_cq()
dequeue_cq()
display_cq()
