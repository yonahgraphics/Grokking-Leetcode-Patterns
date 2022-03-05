class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


# Time Complexity: O(n) since we process every node atmost once
# Space Complexity: O(1) since we have atmost 3 nodes (constant) on the stack
# Alvin says it's O(n)
def dfs(root):
    if root is None:
        return []
    stack = []
    result = []
    stack.append(root)
    while len(stack) > 0:
        curr = stack.pop()
        result.append(curr.val)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return result

# Time complexity: O(n) since every node is visted once and once only
# Space complexity: O(h), where h is the height of the tree
def dfsRecursive(root):
    if root is None:
        return []
    res = [root.val]
    leftValues = dfsRecursive(root.left)
    rightValues = dfsRecursive(root.right)
    res.extend(leftValues)
    res.extend(rightValues)
    return res





if __name__ == "__main__":
    #      A
    #     / \
    #    B   C
    #   /\    \
    #  E  F    G

    A = Node("A")
    B = Node("B")
    C = Node("C")
    E = Node("E")
    F = Node("F")
    G = Node("G")

    A.left  = B
    A.right = C
    B.left  = E
    B.right = F
    C.right = G

    print(dfs(A))
    print(dfsRecursive(A))



