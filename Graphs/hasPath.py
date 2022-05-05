graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
        }


#Iterative Approach (BFS)
# Time Complexity: O(e), where e is the number of edges
# Space complexity: O(n) in the worst case where a node is connected to all the other nodes
def hasPath(graph, source, destn):
    queue = [source]
    visited = set()

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == destn:
            return True
        visited.add(curr)
        for node in graph[curr]:
            if node not in visited:
                queue.append(node)
    return False


#Iterative Approach (DFS)
# If v is the number of vertices and e is the number of edges, then,
# Time Complexity: O(e), where e is the number of edges
# Some people say time complexity = O(v+e)
# Space complexity: O(v) in the worst case where we have to node is connected to all the other nodes

# Alternatively
#-------------------------
# If n represents the number on nodes in the graph
# We can say, Time Complexity: O(n^2) since in the worst case there can be a pair on edges btn every two nodes
# Space Complexity: O(n)

def hasPathDFS(graph, source, destn):
    stack = [source]
    visited = set()

    while len(stack) > 0:
        curr = stack.pop()
        if curr == destn:
            return True
        visited.add(curr)
        for node in graph[curr]:
            if node not in visited:
                stack.append(node)
    return False


def DfsRecursive(graph, source, destn, visited = set()):
    if source not in visited:
        if source == destn:
            return True
        visited.add(source)
        for node in graph[source]:
            res = DfsRecursive(graph, node, destn)
            if res == True:
                return True
        return False


if __name__ == "__main__":
    print(hasPath(graph, 'a', 'f'))
    print(hasPathDFS(graph, 'a', 'f'))
    print(DfsRecursive(graph, 'a', 'f'))


    
