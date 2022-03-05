# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def longestSubStringWithoutRepeatingChar(String): # O(n)
    visited = set()
    l = 0
    max_len = 0
    r = 0
    
    while r < len(String):
        while String[r] in visited:
            visited.remove(String[l])
            l += 1
        visited.add(String[r])
        max_len = max(max_len, r-l + 1)
        r += 1
    return max_len
    
if __name__ == "__main__":
    print(longestSubStringWithoutRepeatingChar("abcad"))
