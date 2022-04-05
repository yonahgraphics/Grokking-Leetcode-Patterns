'''
Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
The function should return a boolean indicating whether or not the linked list contains the target.
'''
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    
# Time complexity: O(n)
# Space complexity: O(1)

# Iterative
def linked_list_find(head, target):
    if head is None:
        return False
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    return False
    
def linked_list_find1(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)
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

    print(linked_list_find(a, "K"))
    print(linked_list_find1(a, 'k'))

