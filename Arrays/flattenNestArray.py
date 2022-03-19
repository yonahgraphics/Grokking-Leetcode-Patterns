'''
You are given a nested list of integers nestedList. '
Each element is either an integer or a list whose elements 
may also be integers or other lists. Implement a function to flatten it.

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
'''

# Time Complexity: O(n*m), where n is the length of  the 2d array and
# n is the average length of the nested array
# Space complexity: O(n*m)
def flatten2DArray(nums, res = []):
    for array in nums:
        if type(array) == int:
            res.append(array)
        else:
            flatten2DArray(array, res)
    return res
print(flatten2DArray([3, [1,2,3, [1,2,1]], 6, [5,6,7], [9]]))
