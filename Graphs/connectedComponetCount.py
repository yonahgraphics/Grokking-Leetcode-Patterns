'''
Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.
'''
def dfs(graph, source, visited):
    if source not in visited:
        visited.add(source)
        for node in graph[source]:
            dfs(graph, node, visited)

def connectedComponentsCount(graph, visited=set()):
    count = 0
    for node in graph.keys():
        if node in visited:
            continue
        dfs(graph, node, visited)
        count += 1
    return count


if __name__ == "__main__":
    graph1 = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
} #----->2


graph2 = {
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
} # ---> 1

graph3 = {
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
} #----> 5
print(connectedComponentsCount(graph3))
