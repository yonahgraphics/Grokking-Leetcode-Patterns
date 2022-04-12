"""
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Time complexity: O(n)
# Space complexity: O(1)
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    curr = root
    nxt = root.left if root else None
    while curr and nxt:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left
        curr = curr.next
        if not curr:
            curr = nxt
            nxt = curr.left
    return root
    
        