class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return 'Stack is Empty' if len(self.items)==0 else f'Number of items in stack: {len(self.items)}'
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return 'Stack is Empty' if len(self.items)==0 else f'Popped item: {self.items.pop()}'
    def top(self):
        return 'Stack is Empty' if len(self.items)==0 else f'Top item: {self.items[-1]}'
    def size(self):
        print("Size of stack: ",end="")
        return len(self.items)
obj=Stack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.is_empty())
print(obj.top())
print(obj.size())
print(obj.pop())
print(obj.size())

class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return 'Queue is Empty' if len(self.items)==0 else f'Number of items in queue: {len(self.items)}'
    def enqueue(self,item):
        self.items.append(item)
        print(f'Enqueued item: {item}')
    def dequeue(self):
        return 'Queue is Empty' if len(self.items)==0 else f'Dequeued item: {self.items.pop(0)}'
    def front(self):
        return 'Queue is Empty' if len(self.items)==0 else f'Front item: {self.items[0]}'
    def rear(self):
        return 'Queue is Empty' if len(self.items)==0 else f'Rear item: {self.items[-1]}'
    def size(self):
        print("Size of queue: ",end="")
        return len(self.items)

obj1=Queue()
obj1.enqueue(1)
obj1.enqueue(2)
obj1.enqueue(3)
print(obj1.is_empty())
print(obj1.front())
print(obj1.rear())
print(obj1.size())
print(obj1.dequeue())
print(obj1.size())


from collections import deque
lst=deque()
lst.append(10)
lst.append(20)
lst.append(30)
lst.appendleft(5)
print("Deque after appending elements:", lst)
lst.pop()
lst.popleft()
print("Deque after popping elements:", lst)
