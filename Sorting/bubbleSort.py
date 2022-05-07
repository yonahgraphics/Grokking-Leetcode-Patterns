""""
----------------------------------------------------
                  BUBBLE SORT
----------------------------------------------------
Description:
The algorith works comparing adjacent elements and and swapping them whenever 
they don't matching the sorting criteria. This process continues to the end of the array
"""
# Time complexity: 
# Best case: O(n)
# Average case: O(n^2)
# Worst case: O(n^2)

# Space complexity: Best case: O(1)
def bubbleSort(nums):
    for i in range(len(nums)):
        arrayIsSorted = True
        for j in range(i, len(nums)-1):
            prevIndex = j
            currentIndex = j+1
            if nums[prevIndex] > nums[currentIndex]:
                nums[prevIndex], nums[currentIndex] = nums[currentIndex], nums[prevIndex]
                arrayIsSorted = False 
        if arrayIsSorted: break # If we receive a sorted list, we really dnt want to sort it
        # We can use a flag to detect if it is sort and break out of the loop, reducing the 
        # time complexity to O(n)
            
    return nums
print(bubbleSort([4,5,2,3]))
