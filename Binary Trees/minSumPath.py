import math

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

# Recursion
# Time Complexity: O(n) since we process every node atmost once
# Space Complexity: O(n) since we make exactly n function calls
def minSumPathRecursive(root):
    if root is None:
        return math.inf # We can't use 0 b'se for negative values, the operation
        # min(minSumPathLeft, minSumPathRight) will return 0 instead of a negative number
        # Thus will cause an error.

    #When we reach the leaf node
    if root.left == None and root.right == None:
        return root.val
    minSumPathLeft = minSumPathRecursive(root.left)
    minSumPathRight = minSumPathRecursive(root.right)
    return root.val + min(minSumPathLeft, minSumPathRight)

if __name__ == "__main__":
    #      1
    #     / \
    #    2   3
    #   /\    \
    #  4  5    6


    A = Node(1)
    B = Node(2)
    C = Node(3)
    E = Node(4)
    F = Node(5)
    G = Node(6)

    A.left  = B
    A.right = C
    B.left  = E
    B.right = F
    C.right = G

    print(minSumPathRecursive(A))
    



