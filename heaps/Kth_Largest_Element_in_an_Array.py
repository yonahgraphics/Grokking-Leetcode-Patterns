""""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

# Approach 1: Sorting
# Time complexity: O(nlogn)
# Space complexity: O(1)
def findKthLargest(self, nums, k):
    nums.sort(reverse = True)
    return nums[k-1]

# Approach 2: Using a maxheap
# Time complexity: O(klogn)
# Space complexity: O(n)
import heapq
def findKthLargest(self, nums, k):
    heap = []

    for i in range(len(nums)):
        heapq.heappush(heap, -1*nums[i])
    while k > 0:
        K_largest = -1*(heapq.heappop(heap))
        k -= 1
    return K_largest

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
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i
