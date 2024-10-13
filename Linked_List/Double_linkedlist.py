class Node:
    def __init__(self,value=0, next=None, prev=None):
        self.value=value
        self.next=next
        self.prev=prev 
def visit(head):
    while head:
        print(head.value, end=" -> ") 
        head=head.next     
first=Node(1)
second=Node(2)
third= Node(3)
first.next=second
second.prev=first
second.next=third
third.prev=second
visit(first)