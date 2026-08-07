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
    def reverse(self): 
        prev=None
        curr=self.head
        while(curr!=None):
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        self.head=prev


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
    def insert(self, pos, val):
        curr=self.head
        count=0
        prev_node=None
        new_node=Node(val)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return
        else:
            try:
                while(count!=pos):
                    prev_node=curr
                    curr=curr.next
                    count+=1
        
            except:
                print("Invalid position")
                return 
            
            new_node.next=curr
            prev_node.next=new_node
    def delete(self, val):
        curr=self.head
        Found=False
        prev_node=None
        if curr.val==val:
            
            self.head=curr.next
            Found=True
            del curr
            return
        else:
            while(curr!=None):
                if curr.val!=val:
                    prev_node=curr
                    curr=curr.next
                    
                elif curr.val==val:
                    Found=True
                    
                    break
            if Found==True:   
                prev_node.next=curr.next
                del curr
                print(Found)
                return Found
            else:
                print("Value not found")
                return 
            
                

            

node1=SinglyLinkedList()
node1.append(5)
node1.append(10)
node1.append(7)


node1.insert(0, 15)
node1.traverse()
    
node1.delete(5)
node1.traverse()
node1.reverse()
node1.traverse()
print('\n')
node1.traverse()
node1.traverse()