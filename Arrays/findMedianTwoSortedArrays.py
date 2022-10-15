"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""


# Time complexity: O(m+n)
# Space complexity: O(m+n)
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    merged = []

    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    if i <len(nums1):
        merged.extend(nums1[i:])
    else:
        merged.extend(nums2[j:])
    low = 0
    high = len(merged) - 1

    mid = (low + high)//2

    if len(merged)%2 == 0:
        median = (merged[mid] + merged[mid + 1]) /2
    else:
        median = merged[mid]

    return median

    if __name__ == "__main__":
        nums1, nums2 = [1,2,3,4], [4,6,7]
        print(findMedianSortedArrays(nums1, nums2))
