# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

#Time complexity : O(p+q), where p+q is a number of nodes in the two trees,
# since one visits each node exactly once.

# Space complexity : O(log(p+q)) in the best case of completely balanced
# tree and O(p+q) in the worst case of completely unbalanced tree,
# to keep a recursion stack.

    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p and q or not q and p:
            return False

        if p.val != q.val:
            return False

        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)
        return isLeftSame and isRightSame