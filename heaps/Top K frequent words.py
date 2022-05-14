"""
692. Top K Frequent Words
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the 
number of occurrence being 4, 3, 2 and 1 respectively.
"""
# Approach: Using a maxheap
# Time complexity: O(klogn)
# Space complexity: O(n)
import heapq
def topKFrequent(words, k):
    heap = []
    wordToCountMap = {}
    result = []

    for word in words:
        if word not in wordToCountMap:
            wordToCountMap[word] = 1
        else:
            wordToCountMap[word] += 1

    for word, freq in wordToCountMap.items():
        heapq.heappush(heap, (-freq, word))

    while k > 0:
        _, word = heapq.heappop(heap)
        result.append(word)
        k -= 1
    return result