'''
largest component
Write a function, largestComponent, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.
'''

#Time complexity: O(e)
#Space complexity: O(n)
import math
def dfs(graph, source, visited):
    count = 0
    if source not in visited:
        visited.add(source)
        count += 1
        for node in graph[source]:
            count += dfs(graph, node, visited)
    return count
        
def connectedComponentsCount(graph, visited=set()):
    maxCount = -math.inf
    for node in graph.keys():
        if node in visited:
            continue
        count = dfs(graph, node, visited)
        maxCount = max(maxCount, count)
        
    return maxCount


if __name__ == "__main__":
    graph = {
    '0': ['8', '1', '5'],
    '1': ['0'],
    '5': ['0', '8'],
    '8': ['0', '5'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['3', '2']
    } # -> 4

    graph1 = {
    1: [2],
    2: [1,8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
    } # -->6
print(connectedComponentsCount(graph1))
