class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


# Time Complexity: O(n), since we visit every node only once
# Space complexity:  O(n)
def treeIncludesRecusion(root, target):
    # check for empty tree
    if root is None:
        return False
    # check if root is target
    if root.val == target:
        return True
    # check if left includes
    resultLeft  =  treeIncludesRecusion(root.left, target)
    # check if right includes
    resultRight =  treeIncludesRecusion(root.right, target)
    #return result
    return resultLeft or resultRight
    #     return True
    # return False
    
# Time Complexity: O(n), since we visit every node only once
# And we assuem we use an effecient implementation of a stack 
# Where push and pop operations are both O(1) each
# Space complexity: O(3) === O(1), Alvin O(n)
def treeIncludesDFS(root, target):
    if not root:
        return False
    stack = []
    stack.append(root)

    while len(stack) > 0:
        curr = stack.pop()
        if curr.val == target:
            return True
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return False

# Time Complexity: O(n), since we visit every node only once
# And we assuem we use an effecient implementation of a queue 
# Where push and pop operations are both O(1) each
# Space complexity: O(3) === O(1), Alvin O(n)
def treeIncludesBFS(root, target):
    if not root:
        return False
    queue = []
    queue.append(root)

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr.val == target:
            return True
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return False


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

    print(treeIncludesRecusion(A, "K"))
    print(treeIncludesDFS(A, "K"))
    print(treeIncludesBFS(A, "K"))



