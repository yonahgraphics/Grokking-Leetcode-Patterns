# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def longestSubStringWithoutRepeatingChar(String): # O(n)
    visited = set()
    l, r = 0,0
    max_len = 0

    while r < len(String):
        if String[r] in visited:
            visited.remove(String[l])
            l += 1
        else:
            visited.add(String[r])
            max_len = max(max_len, r-l + 1)
            r += 1
    return max_len

if __name__ == "__main__":
    print(longestSubStringWithoutRepeatingChar("abcad"))
