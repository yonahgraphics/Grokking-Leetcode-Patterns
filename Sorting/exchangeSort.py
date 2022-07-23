""""
----------------------------------------------------
    EXCHANGE SORT|| BUBBLE SORT VARIANT
----------------------------------------------------
Description:
The algorith works comapring each element with the rest of the elements starting with the first
and swapping them whenever they don't matching the sorting order.
"""
# Time complexity: 
# Best case: O(n^2)
# Average case: O(n^2)
# Worst case: O(n^2)

# Space complexity: Best case: O(1)
def exchangeSort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            prevIndex = i
            currentIndex = j
            if nums[prevIndex] > nums[currentIndex]:
                nums[prevIndex], nums[currentIndex] = nums[currentIndex], nums[prevIndex]
    return nums
print(exchangeSort([4,3,7]))
