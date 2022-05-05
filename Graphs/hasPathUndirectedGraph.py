# Helper function
def makeGraph(edges):
    # Constructin the graph
    graph = {}
    for node1, node2 in edges:
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

# bfs solution
# Time Complexity: O(e), where e is the number of edges
# Some people say time complexity = O(v+e)
# Space complexity: O(v) in the worst case where we have to node is connected to all the other nodes

def hasPath1(edges, source, destn):
    graph = makeGraph(edges)
    visited = set()
    queue = [source]
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == destn:
            return True
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append(neighbour)
    return False

# dfs solution
def hasPath2(edges, source, destn):
    graph = makeGraph(edges)
    visited = set()
    stack = [source]
    while len(stack) > 0:
        curr = stack.pop()
        if curr == destn:
            return True
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                stack.append(neighbour)
    return False

# Recursively
def hasPath3(graph, source, destn, visited=set()):
    if source in visited:
         return False
    if source == destn:
        return True
    visited.add(source)
    for node in graph[source]:
        if hasPath3(graph, node, destn, visited) == True:
            return True
    return False
    

# Given edges
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'], 
    ['o', 'n'],
    # ['j', 'k'],
    # ['k', 'j']
    ]

if __name__ == "__main__":
    graph = makeGraph(edges)
    print(hasPath1(edges, 'k', 'm'))
    print(hasPath2(edges, 'k', 'm'))
    print(hasPath3(graph, 'k', 'm'))
    
    

    