''''
Given the head of a LinkedList, return the sum of values in that LinkedList
'''
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


# Time Complexity: O(n)
# Space Complexity: O(n) due to the values list
def sumListIterative(head):
    totalVal = 0
    curr = head
    while curr is not None:
        totalVal += curr.val
        curr = curr.next
    return totalVal

# Time complexity: O(n)
# Space complexity: O(n) due to the call stack
def sumListRecursive(head):
    if head is None:
        return 0
    return head.val + sumListRecursive(head.next)


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(-1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(sumListIterative(a))
    print(sumListRecursive(a))

    