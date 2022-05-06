""""
----------------------------------------------------
                  SELECTION SORT
----------------------------------------------------
Description:
The algorith works my maintaining a sorted portion on the left of the array
and an unsorted portion on the right.
First, we take the first element as the min/max, then check the remainder of the 
array to confirm this assumption. If we find a new minimum, we update the index of the 
minimum. At the end of this, we swap the new minimum with the current minimum as the algorithm 
continues
"""
# Time complexity: 
# Best case: O(n^2)
# Average case: O(n^2)
# Worst case: O(n^2)

# Space complexity: O(1)
def selectionSort(nums):
    for i in range(len(nums)-1):
        idx_min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[idx_min]:
                idx_min = j
        nums[idx_min], nums[i] = nums[i], nums[idx_min]
    return nums
print(selectionSort([4,5,2,3]))