"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
# Time complexity: O(mn) where m = length of input array, and n = length of shortest string
#  in the input array
# Space complexity: O(1)
def longestCommonPrefix(strs):
    firstString = strs[0]
    res = ""
    
    for i in range(len(firstString)):
        for s in strs:
            indexOutOfBounds = (i == len(s))
            if indexOutOfBounds or firstString[i] != s[i]:
                return res
        res += firstString[i]
    return res