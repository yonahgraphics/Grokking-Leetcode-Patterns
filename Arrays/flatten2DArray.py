# Time Complexity: O(n*m), where n is the length of  the 2d array and nis the length of the inner array
# Space complexity: O(n*m)
def flatten2DArray(nums):
    flatenedArray = []
    for array in nums:
        flatenedArray.extend(array)
    return flatenedArray
    
print(flatten2DArray([[1,2,3], [5,6,7], [9]]))