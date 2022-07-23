"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Link: https://leetcode.com/problems/binary-tree-right-side-view/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

# Time complexity: O(n)
# Space complexity:O(n)
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    queue = deque()
    queue.append(root)
    res = []
    
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            curr = queue.popleft()
            if i == size - 1:
                res.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return res




# BINARY TREE LEFT VIEW

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []
        
        while len(queue) > 0:

            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == size - 1:
                    res.append(curr.val)
                
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
        return res
        
    