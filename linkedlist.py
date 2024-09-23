class Node:
    def __init__(self,value):
        self.data=value
        self.next =None
a=Node(1)
b=Node(2)
c=Node(3)     
# i have made induidual node and connect them to from a LL
a.next=b
b.next=c

class LinkedList:
    def __init__(self):
        #empty linked list
        self.head =None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self,value):
            new_node=Node(value)
            new_node.next =self.head
            self.head = new_node
            self.n+=1

    def __str__(self):
        result=''
        curr = self.head
        while curr!=None:
            result=result+str(curr.data)+'->'
            curr=curr.next
        return result[:-2]

    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
                # i aam at the last node
                curr.next=new_node
            self.n+=1

    def insert_after(self,after,value):
        new_node=Node(value)
        curr=self.head
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next
        if curr!=None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return 'item not found'
    def clear(self):
        self.head=None
        self.n=0

L=LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)


L.append(2)
L.insert(5,70)
print(L)        