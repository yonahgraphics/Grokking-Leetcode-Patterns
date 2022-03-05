'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

Leetcode link: https://leetcode.com/problems/find-the-duplicate-number/

Also checkout: https://leetcode.com/problems/linked-list-cycle-ii/
'''

'''
Proof
----------------------------
Proving that at least one duplicate must exist in numsnums is an application of the pigeonhole principle.
 Here, each number in numsnums is a "pigeon" and each distinct number that can appear in numsnums is a "pigeonhole." 
 Because there are n+1n+1 numbers and nn distinct possible numbers, the pigeonhole principle implies that if 
 you were to put each of the n + 1n+1 pigeons into nn pigeonholes, at least one of the pigeonholes would have 2 
 or more pigeons.
'''

# Naive Approach1
# Sorting
'''
Complexity Analysis

Time Complexity: O(nlogn)

Sorting takes O(nlogn) time. This is followed by a linear scan, resulting in 
a total of O(nlogn) + O(n) = O(nlogn) time.

Space Complexity: O(logn) or O(n)

The space complexity of the sorting algorithm depends on the implementation of each programming language:

In Java, Arrays.sort() for primitives is implemented using a variant of the Quick Sort algorithm,
 which has a space complexity of O(logn)
In C++, the sort() function provided by STL uses a hybrid of Quick Sort, Heap Sort and Insertion Sort,
 with a worst case space complexity of O(logn)
In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space 
complexity of O(n)
'''
def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]


# Naive Approach2
# sets
'''
Algorithm
In order to achieve linear time complexity, we need to be able to insert elements into a data structure
 and look them up in constant time. A HashSet/unordered_set is well suited for this purpose. Initialize
an empty hashset, seenseen.

Iterate over the array and first check if the current element exists in the hashset (seenseen).

If it does exist in the hashset, that number is the duplicate and can be returned right away.
Otherwise, insert the current element into seenseen, move to the next element in the array and repeat step 2.


Complexity Analysis

Time Complexity: O(n)
HashSet insertions and lookups have amortized constant time complexities. Hence, this algorithm requires 
linear time, since it consists of a single for loop that iterates over each element, looking up the element
and inserting it into the set at most once.

Space Complexity: O(n)
We use a set that may need to store at most nn elements, leading to a linear space complexity of O(n).
'''

def findDuplicate1(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

'''
Floyd's tortoise and hare cycle detection algorithm
'''
def findDuplicate2(nums):
    tortoise, hare = 0,0
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
    while hare != tortoise:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        
    hare = 0
    while True:
        hare = nums[hare]
        tortoise = nums[tortoise]
        if hare == tortoise:
            return hare
        

if  __name__ == "__main__":
    print(findDuplicate([1,2,3,3,4]))
    print(findDuplicate1([1,2,3,3,4]))
    print(findDuplicate2([1,2,3,3,4]))