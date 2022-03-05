class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

# Recursion
# Time Complexity: O(n) since we process every node atmost once
# Space Complexity: O(n) since we make exactly n function calls
def treeSumRecursive(root):
    if root is None:
        return 0
    # sum left
    sumLeft = treeSumRecursive(root.left)
    # sum right
    sumRight = treeSumRecursive(root.right)
    # add root to the two sums and return
    return root.val + sumLeft + sumRight

# BFS Iterative
# Time Complexity: O(n) since we process every node atmost once
# Space Complexity: O(1) since we have atmost 3 nodes (constant) on the queue
# Alvin says it's O(n)
def treeSumIterativeBFS(root):
    if root is None:
        return 0
    sum = 0
    queue = []
    queue.append(root)
    while len(queue) > 0:
        curr = queue.pop(0)
        sum += curr.val
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return sum

# BFS Iterative
# Time Complexity: O(n) since we process every node atmost once
# Space Complexity: O(1) since we have atmost 3 nodes (constant) on the stack
# Alvin says it's O(n)
def treeSumIterativeDFS(root):
    if root is None:
        return 0
    sum = 0
    stack = []
    stack.append(root)
    while len(stack) > 0:
        curr = stack.pop()
        sum += curr.val
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return sum



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

    print(treeSumRecursive(A))
    print(treeSumIterativeBFS(A))
    print(treeSumIterativeDFS(A))



