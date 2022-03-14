'''
Leetcode link: https://leetcode.com/problems/reverse-string/

344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''

#Time Complexity: O(n) since we traverse the sting only once
#Space Complexity: O(1) since we don't use any extra space
def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

if __name__ == "__main__":
    print(reverseString(['b', 'o', 'x']))
        