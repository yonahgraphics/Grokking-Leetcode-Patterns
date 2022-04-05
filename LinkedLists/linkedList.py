class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


# Time Complexity: O(n)
# Space Complexity: O(1)
def printListIterative(head):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next
    
# Time complexity: O(n)
# Space complexity: O(n)
def printListRecursive(head):
    if head is None:
        return
    print(head.val)
    printListRecursive(head.next)


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

    # printListIterative(a)
    printListRecursive(a)

    