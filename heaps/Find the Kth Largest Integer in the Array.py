
"""
1985. Find the Kth Largest Integer in the Array

You are given an array of strings nums and an integer k. Each string in nums represents 
an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], 
"2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.
Example 1:

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
Example 2:

Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".
"""

# Approach 1: Sorting
# Time complexity: O(nlogn)
# Space complexity: O(1)
def kthLargestNumber(self, nums, k):
    for i, num in enumerate(nums):
        nums[i] = int(num)
    nums.sort(reverse = True)
    return str(nums[k-1])

# Approach 2: Using a maxheap
# Time complexity: O(klogn)
# Space complexity: O(n)
import heapq
def findKthLargest(self, nums, k):
    heap = []

    for i in range(len(nums)):
        heap.append(-1*int(nums[i]))
    heapq.heapify(heap)
    while k > 0:
        K_largest = -1*(heapq.heappop(heap))
        k -= 1
    return str(K_largest)

# Approach 3: Using Quick select
# Time complexity: O(n) in the best case, worst case is O(n^2)
# Space complexity: O(1)
class Solution(object):
    def findKthLargest(self, nums, k):
        return self.qs(nums, 0, len(nums)-1, k)
    
    def qs(self, arr, l, r, k):
        p = self.partition(arr, l, r)
        if (k-1) == p:
            return arr[p]
        elif (k-1) > p:
            return self.qs(arr, p + 1, r, k)
        else:
            return self.qs(arr, l, p - 1, k)

    def partition(self, arr, l, r):
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if int(arr[j]) > int(pivot):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

