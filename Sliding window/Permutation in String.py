
"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1,
 or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""

#For the naive approach, we can get substrings of size s1 from s2 and sort them
# lexicographically then compare them with the the sorted s1.
# return true if they match and false otherwise
def checkInclusion(s1, s2):
    s1_sorted = sorted(s1)
    l = 0
    r = len(s1)-1
    
    while r < len(s2): #O(n.mlogm)
        substr = s2[l:r+1]
        sorted_substr = sorted(substr)   
        if s1_sorted == sorted_substr:
            return True
        l += 1
        r += 1
    return False


def checkInclusionOptimum(s1, s2): # O(n time complexity), O(26) === O(1) space cpmplexity
    if len(s1) > len(s2): return False
    
    s1Count, s2Count = [0]*26, [0]*26
    numMatches= 0
    l = 0

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    for i in range(26):
        numMatches += (1 if s1Count[i] == s2Count[i] else 0)

    for r in range(len(s1), len(s2)):
        if numMatches == 26:
            return True

        # Expand window
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            numMatches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            numMatches -= 1

        #Shrink window
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            numMatches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            numMatches -= 1
        l += 1
    return numMatches == 26


if __name__ == "__main__":
    print(checkInclusion("fa", "abacus"))
    print(checkInclusionOptimum("fa", "abacus"))
