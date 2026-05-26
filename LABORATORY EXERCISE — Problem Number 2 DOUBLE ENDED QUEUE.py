#MARC RODEN D. FAMERO
#DATA STRUCTURES AND ALGORITHM - DSA (CIST103)
#LABORATORY EXERCISE — Problem Number 2 - DOUBLE ENDED QUEUE

# Deque using one-dimensional array
deque = []

def insert_front(item):
    deque.insert(0, item)

def insert_rear(item):
    deque.append(item)

def delete_front():
    if not deque:
        print("Deque Underflow")
    else:
        print("Deleted from front:", deque.pop(0))

def delete_rear():
    if not deque:
        print("Deque Underflow")
    else:
        print("Deleted from rear:", deque.pop())

def display_deque():
    print("Deque elements:", deque)

# Deque operations
insert_rear(10)
insert_rear(20)
insert_front(5)
display_deque()
delete_front()
delete_rear()
display_deque()
