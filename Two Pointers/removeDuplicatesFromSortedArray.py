# Time Complexity: O(2N) === O(N)
# Space Complexity: O(1)

'''
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
def removeDuplicates(nums):
    i = 1
    for j  in range(1, len(nums)):
        
        if nums[j] == nums[j-1]:
            j += 1 
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    
    return i
    
'''
def removeDuplicates(nums):
        i = 1
        for j  in range(1, len(nums)):
            
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1 
        return i
    
'''
if __name__ == "__main__":
    print(removeDuplicates([1,2,2,3,4,5]))
        