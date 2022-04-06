'''
Given the head of a linkedList, reverse the linkedlist
'''
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

# Iterative approach
# Time complexity: O(n)
# Space complexity: O(1)
def reverseList(head):
    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

if __name__ == "__main__":
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    

