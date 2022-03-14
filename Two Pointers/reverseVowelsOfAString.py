
'''
Leetcode Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
#Time Complexity: O(n) where n is the length of the string, since we traverse the string once
#Space Complexity: O(n) since we convert a string to a list
def reverseVowels(s):
    vowels = {'a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    s = list(s)
    i = 0
    j = len(s)-1
    
    while i < j:
        if s[i] not in vowels:
            i += 1
            continue
        if s[j] not in vowels:
            j -= 1
            continue
            
        s[i], s[j] = s[j], s[i]
        i +=1
        j -= 1
    return "".join(s)
            
if __name__ == "__main__":
    print(reverseVowels("hello"))
    
    
