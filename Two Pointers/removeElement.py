'''
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place.
 The relative order of the elements may be changed.
'''

# Time Complexity: O(2N) === O(N)
# Space Complexity: O(1)
def removeElement(self, nums, val):
    i = 0
    for j in range(0, len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return  i

if __name__ == "__main__":
    print(removeElement([1,2,3,3,2,3,5], 3))
            
                
                
        