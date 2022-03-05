'''
shortest path

Write a function, shortestPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB).
The function should return the length of the shortest path between A and B.
Consider the length as the number of edges in the path, not the number of nodes.
If there is no path between A and B, then return -1.
'''
# class Node:
#     def __init__(self, val, dist=0):
#         self.val = val
#         self.dist = dist

def makeGraph(edgeList):
    graph = {}
    for node1, node2 in edgeList:
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

    
# Time Complexity: O(e), where e is the number of edges
# Some people say time complexity = O(v+e)
# Space complexity: O(v) in the worst case where we have to node is connected to all the other nodes
def shortestPath(edgeList, source, destn):
    graph = makeGraph(edgeList)
    queue = [[source, 0]]
    visited = set()
    while len(queue) > 0:
        curr, dist = queue.pop(0)
        if curr == destn:
            return dist
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append([neighbour, dist + 1])
    return -1


if __name__ == "__main__":
    edges = [
            ['w', 'x'],
            ['x', 'y'],
            ['z', 'y'],
            ['z', 'v'],
            ['w', 'v']
            ] # ---> 2
    print(shortestPath(edges, 'w', 'z'))



