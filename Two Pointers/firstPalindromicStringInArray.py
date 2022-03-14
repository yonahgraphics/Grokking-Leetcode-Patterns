'''
Leetcode link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
2108. Find First Palindromic String in the Array
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.

Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
'''
# Time complexity: O(n*m) where n is the length of the array and m ,
# is the average length of a string in the array.
# Space complexity: O(1)

def firstPalindrome(words):
    # Function to check if a given string is a palindrome or not
    def isPalindrome(s):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    for word in words:
        if isPalindrome(word):
            return word
    return ""

       
                    
                    
        