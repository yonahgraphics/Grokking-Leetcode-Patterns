""""
----------------------------------------------------
                  INSERTION SORT
----------------------------------------------------
"""
# Time complexity: O(n^2)
# Space complexity: O(1)
def insertionSort(nums):
    for i in range(1, len(nums)):
        # temp  = nums[i]
        for j in range(i):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
print(insertionSort([4,5,2,3]))
