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

# Time complexity: O(n)
# Space complexity: O(n) due to the call stack
def reverseList1(head, prev = None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverseList1(next, prev)


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
    

