"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

# Approach 1: Using a hashmap
# Time complexity: O(nlogn)
# Space complexity: O(n)

# Fails this case, I don't know why
#[4,1,-1,2,-1,2,3], k = 2
def topKFrequent(self, nums, k):
    numToCountMap = {}
    result = []
    for num in nums:
        if num not in numToCountMap:
            numToCountMap[num] = 1
        else:
            numToCountMap[num] += 1
    # Sort dict in descending order by value
    sorted_map = dict(sorted(numToCountMap.items(), key=lambda x: x[1], reverse=True))
    print(sorted_map)
    i = 0
    for key in sorted_map.keys():
        if i == k: 
            break
        result.append(key)
        i += 1
    return result


# Approach 2: Using a maxheap
# Time complexity: O(klogn)
# Space complexity: O(n)
import heapq
def topKFrequent(self, nums, k):
    heap = []
    numToCountMap = {}
    result = []
    
    for num in nums:
        if num not in numToCountMap:
            numToCountMap[num] = 1
        else:
            numToCountMap[num] += 1
            
    for num, freq in numToCountMap.items():
        heap.append((-freq, num))
    heapq.heapify(heap)
    
    while k > 0:
        _, num = heapq.heappop(heap)
        result.append(num)
        k -= 1
    return result
        
    
# Approach 3: Using BucketSort
# Time complexity: O(n)
# Space complexity: O(n)
def topKFrequent(self, nums, k):
        numFrequencyMap = {}
        result = []
        for num in nums:
            numFrequencyMap[num] = 1 + numFrequencyMap.get(num, 0)
        freqArray = [[] for i in range(len(nums) + 1)]
        for key, value in numFrequencyMap.items():
            freqArray[value].append(key)

        i = len(freqArray)-1
        while i >= 0:
            for num in freqArray[i]:
                result.append(num)
                if len(result) == k:
                    return result
            i -= 1
        return-1
    