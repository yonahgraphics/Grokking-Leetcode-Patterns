"""

Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Aproach 1: Recursion
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree, in the worst case, h == n
def postorderTraversal(root):
    res = []
    def traverseTree(root):
        if not root:
            return
        traverseTree(root.left)
        traverseTree(root.right)
        res.append(root.val)
    
    traverseTree(root)
    return res