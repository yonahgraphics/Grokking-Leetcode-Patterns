# Best runtime O(n2)
# Worst runtime O(n3)

# All we do is start at a particular index and expand out to find
# all palindromic substrings which the char at that index is a centre of
# Do this for both odd and even palindromes while left and right pointer are inbounds.
# Problem: https://leetcode.com/problems/palindromic-substrings/
def countSubstrings(s):
        res = 0
        for i in range(len(s)): # O(n)
            l = r = i
            # Counts odd palindromes
            while l >= 0  and r < len(s) and s[l] == s[r]: # O(n)
                    res += 1
                    l -= 1
                    r += 1
                    
            # Coounts even palindromes
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
        return res



#### Cleanedup version
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            
            # Counts odd palindromes
            res += self.countPalindrome(s, l, r)
            
            l = i
            
            r = i + 1
            # Coounts even palindromes
            res += self.countPalindrome(s, l, r)
                                
        return res
    
    def countPalindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
        
if __name__ == "__main__":
    print(countSubstrings("aaa"))