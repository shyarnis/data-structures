# Implementation of queue as a list(array)

class Queue:

    # create a empty Queue named 'items'
    def __init__(self):
        self.items = []
    
    # check if queue is empty
    def is_empty(self):
        return self.items == []
    
    # add new item to 'rear' of queue
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # remove item from 'front' of queue
    def dequeue(self):
        return self.items.pop()
    
    # length of queue
    def length(self):
        return len(self.items)
    

# # Initialization of queue
# q = Queue()

# q.enqueue(12)
# q.enqueue(33)
# q.enqueue(55)
# q.enqueue(85)

# # queue = 85-->55-->33-->12
# # items = [85, 55, 33, 12]
# print(q.length())       # 4

# print(q.dequeue())      # 12
# print(q.dequeue())      # 33
# print(q.dequeue())      # 55
# print(q.dequeue())      # 85
