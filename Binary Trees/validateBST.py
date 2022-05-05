"""
https://leetcode.com/problems/validate-binary-search-tree/
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(n)
# Space complexity: O(n)
def isValidBST(root):
    def dfs(root, left, right):
        if root is None:
            return True
        if root.val >= right or root.val <= left :
            return False
        validLeft = dfs(root.left, left, root.val)
        validRight = dfs(root.right, root.val, right)
        return validLeft and validRight
    return dfs(root, float("-inf"), float("inf"))
    