'''
The below algorithm’s time complexity will be O(N), 
where N is the number of characters in the input string. 
The outer for loop runs for all characters, processing each character only once;
 therefore, the time complexity of the algorithm will be O(N).
The algorithm’s space complexity is O(K+1), as we will be storing 
a maximum of K+1 characters in the HashMap, wchich is asymptotically equivalent to O(K)
'''

import math
def longestSubStringWithKSiatinctCharacters(string, K): # O(n)
    visited = {}
    l = 0

    max_len = -math.inf
    
    for r in range(len(string)):
        visited[string[r]] = r # The map will have atmost K+1 elements at a time, wc is constant
        if len(visited) > K:
            # remove the left most element
            min_idx = min(visited.values()) # Sort is KlogK which is a constant
            visited.pop(string[min_idx])
            l = min_idx + 1
        max_len = max(max_len, r-l + 1)
    return max_len
    
if __name__ == "__main__":
    print(longestSubStringWithKSiatinctCharacters(("ykokknaj"), 3))
            
 