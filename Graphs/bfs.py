graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
        }

# Time Complexity: O(e), where e is the number of edges
# Some people say time complexity = O(v+e)
# Space complexity: O(v) in the worst case where we have to node is connected to all the other nodes

def bfs(graph, source):
    queue = [source]
    visited = set()
    res = []
    while len(queue) > 0:
        curr = queue.pop(0)
        res.append(curr)
        visited.add(curr)
        for node in graph[curr]:
            if node not in visited:
                queue.append(node)
    return res

if __name__ == "__main__":
    print(bfs(graph, 'a'))