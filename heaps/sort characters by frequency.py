"""
451. Sort Characters By Frequency
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
"""
# Using a maxheap
# Time complexity: O(nlogn)
# Space complexity: O(n)
import heapq
def frequencySort(s):
    charFreq = {}
    for char in s:
        charFreq[char] = 1 + charFreq.get(char, 0)
    maxheap = []
    
    for char, freq in charFreq.items():
        maxheap.append((-freq, char))
    heapq.heapify(maxheap)
    result = ""
    
    while maxheap:
        freq, char  = heapq.heappop(maxheap)
        result += char*(-freq)
        
    return result

print(frequencySort("oobbox"))