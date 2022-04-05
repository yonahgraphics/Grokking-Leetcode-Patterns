'''
Write a function, get_node_value, that takes in the head of a linked list and an index. 
The function should return the value of the linked list at the specified index.
If there is no node at the given index, then return None.
'''
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

# Time complexity: O(n)
# Space complexity: O(1)
def get_node_value(head, index):
    curr = head
    i = 0
    while curr is not None:
        if index == i:
            return curr.val
        i += 1
        curr = curr.next
    return None

# Time complexity: O(n)
# Space complexity: O(n) due to the call
def get_node_value1(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value1(head.next, index-1)

    

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

    print(get_node_value(a, 2))
    print(get_node_value1(a, 2))
