''''
Given an array of sorted numbers and a target sum, find a pair in the array whose
sum is equal to the given target.
You can assume the input will be sorted always
'''

# Use a nested loop to get all possible combinations of the sum of two
# Compare with the target
# Return the indexes if they equal the target
def twoSumNaive(arr, target): # O(n2) time, O(1) space
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return -1


# Use a hashmap to keep all visited nums
# Check if the diff btn the target and nus starting with the second one are
# in the hasmap, if so, return the idx of the current num and the idx in 
# the map that corresponds to the diff
def twoSumOptimum(arr, target): # O(n) time, O(n) space
    visited = {} # num : idx

    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in visited:
            return [visited[diff], i]
        
        visited[arr[i]] = i


'''
We can follow the Two Pointers approach. We will start with one pointer pointing to
the beginning of the array and another pointing at the end. At every step, we will
see if the numbers pointed by the two pointers add up to the target sum. If they do,
we have found our pair; otherwise, we will do one of two things:

If the sum of the two numbers pointed by the two pointers is greater than the target sum,
this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement
the end-pointer.
If the sum of the two numbers pointed by the two pointers is smaller than the target sum,'
this means that we need a pair with a larger sum. So, to try more pairs, we can increment
the start-pointer.
'''
#The time complexity of the above algorithm will be O(N), where ‘N’ is the total number 
# of elements in the given array.
#The algorithm runs in constant space O(1).
def twoSumTwoPointer(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        currSum = arr[left] + arr[right]
        if currSum == target:
            return [left, right]
        if currSum > target:
            right -= 1
        else:
            left += 1
    return -1
if __name__ == "__main__":
    print(twoSumOptimum([1,3,4,5], 7))
    print(twoSumNaive([1,3,4,5], 7))
    print(twoSumTwoPointer([1,3,4,5], 7))
  