''''Given the head of a LinkedList, return an Array containing all the values of 
the nodes in the linkedlist
'''
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


# Time Complexity: O(n)
# Space Complexity: O(n) due to the values list
def traverseListIterative(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    return values

# Time complexity: O(n)
# Space complexity: O(n)
def traverseListRecursive(head):
    values = []
    def populateArray(head, values):
        if head is None:
            return
        populateArray(head.next, values)
        values.append(head.val)
    populateArray(head, values)
    return values


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

    print(traverseListRecursive(a))
    print(traverseListIterative(a))

    