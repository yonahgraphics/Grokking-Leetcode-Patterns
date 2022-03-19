'''
Given an array of integers nums which is sorted in ascending order, and an integer target,
 write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.
You must write an algorithm with O(log n) runtime complexity.

Leetcode: https://leetcode.com/problems/binary-search/
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

def BinarySearchRecursive(data, key, low, high):
    # Base case
    if low > high:
        print(key, "not in list")
        return
    
    mid = low + (high - low)//2
    
    if key == data[mid]:
        print(key, "found in the list")
        
    elif key < data[mid]:
        high = mid - 1
        BinarySearchRecursive(data, key, low, high)
    else:
        low = mid + 1
        BinarySearchRecursive(data, key, low, high)


def BinarySearchIterative(data, target):
    data.sort() #nlogn
    found = False
    low = 0
    high = len(data) - 1

    while low <= high and found is False:
        mid = low + (high - low) //2 
        if target == data[mid]:
            found = True
        elif target > mid:
                low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print(target, "found in the list")
    else:
        print(target, "not found in the list")


if __name__ == "__main__":
    BinarySearchRecursive([1,2,4,6,7,8], 8, 0, 5)
    
    
    
     