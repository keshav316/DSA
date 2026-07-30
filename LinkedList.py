class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
# Node1=Node(5)
# Node2=Node(10)
# Node3=Node(7)
# Node4=Node(8)
# Node1.next=Node2
# Node2.next=Node3
# Node3.next=Node4
# print(Node1.val)
# print(Node1.next)
# print(Node1.next.val)

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self, val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new_node
    def traverse(self):
        if self.head==None:
            print("LinkedList is empty")
        else:
            curr=self.head
            while (curr != None):
                print(curr.val,end=" ")
                curr=curr.next
                

node1=SinglyLinkedList()
node1.append(5)
node1.append(10)
node1.append(7)

node1.traverse()
    

