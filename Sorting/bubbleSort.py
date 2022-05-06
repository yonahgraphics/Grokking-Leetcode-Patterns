""""
----------------------------------------------------
                  BUBBLE SORT
----------------------------------------------------
Description:
The algorith works comapring each element with the rest of the elements starting with the first
and swapping them whenever they don't matching the sorting order.
"""
# Time complexity: 
# Best case: O(n)
# Average case: O(n^2)
# Worst case: O(n^2)

# Space complexity: Best case: O(1)
def bubbleSort(nums):
    for i in range(len(nums)-1):
        isSorted = True
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                isSorted = False 
        if isSorted: break # If we receive a sorted list, we really dnt want to sort it
        # We can use a flag to detect if it is sort and break out of the loop, reducing the 
        # time complexity to O(n)
            
    return nums
print(bubbleSort([4,5,2,3]))
