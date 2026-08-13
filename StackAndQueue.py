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