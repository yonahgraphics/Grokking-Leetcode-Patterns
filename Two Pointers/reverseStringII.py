'''
Leetcode: https://leetcode.com/problems/reverse-string-ii/
Reverse String II
Given a string s and an integer k, reverse the first k characters for every 2k
characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less 
than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
'''
#Time Complexity: O(k*n), where n is the leng of the given string
#Space Complexity: O(n)
def reverseStr(s, k):
    r = ''
    for i in range(0, len(s), k*2):
        r += s[i:i+k][::-1] + s[i+k:i+k+k]
    return r
    
if __name__ == "__main__":
    print(reverseStr('abcdefg', 2))