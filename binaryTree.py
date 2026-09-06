class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

node5=Node(5)
node3=Node(3)
node4=Node(4)
node2=Node(2)
node9=Node(9)
node8=Node(8)
node10=Node(10)
node1=Node(1)
node6=Node(6)

node5.left=node3
node5.right=node4
node3.left=node2
node3.right=node9
node4.left=node8
node4.right=node10
node8.left=node1
node8.right=node6

def preorder_traversal(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)
obj=node5
preorder_traversal(obj)
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=" ")
    inorder_traversal(node.right)
obj2=node5
print('\n')
inorder_traversal(obj2)
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=" ")
obj3=node5
print('\n')
postorder_traversal(obj3)

from collections import deque

def level_order(root):
    result=[]
    queue=deque([])
    queue.append(root)

    while len(queue)!=0:
        e=queue.popleft()
        result.append(e.data)
        if e.left:
            queue.append(e.left)
        if e.right:
            queue.append(e.right)
    return result

print('\n')
print(level_order(node5))