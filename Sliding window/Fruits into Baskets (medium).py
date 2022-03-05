'''
This problem is similar to the longest substring with K distinct characters problem
Here K = 2
'''

def totalFruit(self, fruits: List[int]) -> int:
        
        l = 0
        visited = {}
        max_fruits = -1
        
        for r in range(len(fruits)):
            visited[fruits[r]] = r
            if len(visited) > 2:
                min_idx = min(visited.values()) #2log2
                visited.pop(fruits[min_idx])
                l = min_idx + 1
            max_fruits = max(max_fruits, r-l+1)
            
        return max_fruits
        