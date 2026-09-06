class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def traverse(self):
        if self.head==None:
            print("LinkedList is empty")
        else:
            curr=self.head
            while(curr!=None):
                print(curr.val,end=" ")
                curr=curr.next
            print('\n')
    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
    def insert_between(self,pos,val):
        new_node=Node(val)
        if pos==0:
            
            self.insert(val)
            return 
        else:
            curr=self.head
            count=0
            while(count<pos-1):
                curr=curr.next
                count+=1
            if curr==None:
                print("Invalid position")
                return
            new_node.next=curr.next
            new_node.prev=curr
            curr.next=new_node
    def delete(self, pos):
        # Empty list
        if self.head is None:
            return

        curr = self.head

        # Move to the required position
        for i in range(1, pos):
            if curr is None:
                return
            curr = curr.next

        # Position doesn't exist
        if curr is None:
            return

        # Deleting the head
        if curr == self.head:
            self.head = curr.next

            if self.head is not None:
                self.head.prev = None

        # Deleting any other node
        else:
            curr.prev.next = curr.next

            if curr.next is not None:
                curr.next.prev = curr.prev
    def reverse(self):
        if self.head.next is None:
            return
        else:
            prev=None
            curr=self.head
            while(curr!=None):
                front=curr.next
                curr.next=prev
                curr.prev=front
                prev=curr
                curr=front
            self.head=prev   
                

Node1=DoublyLinkedList()
Node1.insert(10)
Node1.traverse()
Node1.append(20)
Node1.append(30)
Node1.traverse()


Node1.reverse()
Node1.traverse()