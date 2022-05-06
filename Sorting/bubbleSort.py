""""
----------------------------------------------------
                  BUBBLE SORT
----------------------------------------------------
Description:
The algorith works comapring each element with the rest of the elements starting with the first
and swapping them whenever they don't matching the sorting order.
"""
# Time complexity: O(n^2)
# Space complexity: O(1)
def selectionSort(nums):
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
print(selectionSort([4,5,2,3]))