""""
----------------------------------------------------
                  INSERTION SORT
----------------------------------------------------
"""
# Time complexity: 
# Best case: O(n)
# Average case: O(n^2)
# Worst case: O(n^2)

# Space complexity: O(1)

def insertionSort(nums):
    for i in range(1, len(nums)):
        while i > 0 and nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1
    return nums
print(insertionSort([4,5,2,3]))
