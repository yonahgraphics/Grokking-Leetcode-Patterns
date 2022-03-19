'''
Given a sorted array of distinct integers and a target value, return 
the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

 Leetcode link: https://leetcode.com/problems/search-insert-position/

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

***PRO TIP***

If you use a recursive approach, then at each stage, you have to make a recursive call.
That means leaving the current invocation on the stack, and calling a new one. 
When you're k levels deep, you've got k lots of stack frame, so the space complexity ends 
up being proportional to the depth you have to search.
With your iterative code, you're allocating one variable (O(1) space) plus a single stack 
frame for the call (O(1) space). Your while loop doesn't ever allocate anything extra, either 
by creating new variables or object instances, or by making more recursive calls. So the only 
space you need, for your whole call, is the O(1) space taken up by the variable you create and the rest of the stack frame.
Whenever you can rewrite a recursive algorithm as a simple iteration, it's worth doing precisely 
because of this reduced space requirement.
'''


# Time Compleexity: O(n)
# Space Complexity: O(1)
def searchInsert1(nums, key):
    for i in range(len(nums)):
        if key == nums[i]:
            return i
        elif key > nums[i]:
            continue
        else:
            return i


# Time Complexity: O(n)
# Space Complexity: O(1)
def searchInsert2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = low  + (high - low)//2
        
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid +1
        else:
            return mid
    return low

# Time Complexity: O(logn)
# Space Complexity: O()
def getCeilingOptimum3(array, key, low, high):
    if low > high:
        return low
    mid = low + (high - low)//2
    if key == array[mid]:
        return mid
    if key < array[mid]:
       high = mid-1
       return getCeilingOptimum(array, key, low, high)
    else:
       low = mid+1
       return getCeilingOptimum(array, key, low, high)
    

if __name__ == "__main__":
    print(searchInsert1([1,2,3,4,7,8], 7))
            
        