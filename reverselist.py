class node:
    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt
    
head = node(1, node(2, node(3, node(4, node(5, None)))))

def display(head):
    while head:
        print head.val, 
        head = head.nxt
    print 
    
display(head)

def reverse(head):
    cur = head
    prev = None
    while cur: 
        nxt = cur.nxt
        cur.nxt = prev
        prev = cur
        cur = nxt
    return prev

head = reverse(head)
display(head)

