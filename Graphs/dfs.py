graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
        }


# Iterative
# Time Complexity: O(e), where e is the number of edges
# Some people say time complexity = O(v+e)
# Space complexity: O(v) in the worst case where we have to node is connected to all the other nodes

def dfs(graph, source):
    stack = [source]
    res = []
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        res.append(curr)
        visited.add(curr)
        for node in graph[curr]:
            if node not in visited:
                stack.append(node)
    return res


# Recursive
def dfsRecursive(graph, source, visited=set()):
    res = []
    if source not in visited:
        visited.add(source)
        res.append(source)
        for node in graph[source]:
           res1 = dfsRecursive(graph, node, visited)
           res.extend(res1)
        return res

if __name__ == "__main__":
    print(dfs(graph, 'a'))
    print(dfsRecursive(graph, 'a'))
