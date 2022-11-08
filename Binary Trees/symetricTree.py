# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center)

# Example
# Input: root = [1,2,2,3,4,4,3]
# Output: true


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)