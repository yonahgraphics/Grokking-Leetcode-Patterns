# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(m+n)
# Space complexity: 
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
    
        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)
        
        return isLeftSame and isRightSame
        