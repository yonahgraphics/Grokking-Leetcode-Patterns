
def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        l = r = i
        # find odd palindromes
        while l >= 0  and r < len(s) and s[l] == s[r]:
            if r - l +1 > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
                
        # find even palindromes
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l +1 > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
    return res

if __name__ == "__main__":
    print(longestPalindrome("boods"))