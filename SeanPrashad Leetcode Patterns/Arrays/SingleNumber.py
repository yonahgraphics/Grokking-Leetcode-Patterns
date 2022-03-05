'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice
 except for one. Find that single one.
You must implement a solution with a linear runtime complexity
and use only constant extra space.

Input: nums = [4,1,2,1,2]
Output: 4

'''
# Aproach 1: HashSet
# This won't work since it violates the constant space requirement
def singleNumber1(nums):
    seen = set()

    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop()


# Approach 2: Bit Manipulation
# The intution is that when you XOR any number with 0 you get back that number
# Also, the order of XOR doesn't change the result
'''
4 ------ 1 0 0
1 ------ 0 0 1
2 ------ 0 1 0
1 ------ 0 0 1
2 ------ 0 1 0
--------------
result = 1 0 0 == 4
If we XOR each column from the right to the left, we get 100, which is 4 and is the missing number
Thus, if we XOR all the numbers, we should get the single number as the result
We can set our intitial result to 0 since we know that  0^anynumber gives back that number
'''
# Time complexity: O(n)
# Space complexity: O(1)
def singleNumber2(nums):
    result = 0 # n^0 = n

    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print(singleNumber1(nums))
    print(singleNumber2(nums))

        