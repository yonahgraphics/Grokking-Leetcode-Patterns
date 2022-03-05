'''
409. Longest Palindrome
Easy
Link: https://leetcode.com/problems/longest-palindrome/submissions/
Given a string s which consists of lowercase or uppercase letters,
 return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2

Since we are interested in only the length of the pandrome, we can use a map
to store the frequency of every character.
Then we can count the length of the palindrome by going thru the map and adding the even
frequency of chars and for odd ones, we take odd-1. Once we finish, there could
be some chars remaining. To know this, we check if the len of the longest palindrome we
found is less than the length of the entire given string. If true, we add 1 to our
result and return the result. If false, then we used all the letters, we just return the
result the way it is
'''

#O(n) time
#O(1) space

def longestPalindrome(s):
    if len(s)  == 0:
        return 1
    map = {} # Constant space O(1) since this map can only be  56 (a-z + A-Z)

    max_len = 0

    for char in s:
        if char in map: # Constant lookup
            map[char] += 1
        else:
            map[char] = 1
    for char in map:
        if map[char] % 2 == 0:
            max_len += map[char]
        else:
            max_len += map[char] - 1

    if max_len < len(s):
        max_len += 1
    return max_len


if __name__ == "__main__":
    print(longestPalindrome("aaarbb"))