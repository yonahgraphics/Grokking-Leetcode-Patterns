class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

# BFS Iterative
# Time Complexity: O(n) since we process every node atmost once
# Space Complexity: O(1) since we have atmost 3 nodes (constant) on the queue
# Alvin says it's O(n)
def bfs(root):
    if root is None:
        return []
    queue = []
    res = []
    queue.append(root)
    while len(queue) > 0:
        curr = queue.pop(0)
        res.append(curr.val)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
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

    print(bfs(A))



