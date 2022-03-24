'''
881. Boats to Save People
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight 
of those people is at most limit.
Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Leetcode link: https://leetcode.com/problems/boats-to-save-people/
'''

# Time Complexity: O(n) + O(nlogn) === O(nlogn)
# Space Comlexity: O(n) due to TimSort()

def numRescueBoats(people, limit):
    people.sort()
    
    numBoats = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        remainder = limit - people[right]
        numBoats += 1
        right -= 1
        
        if left <= right and people[left] <= remainder:
            left += 1
    return numBoats
    
if __name__ == "__main__":
    print(numRescueBoats([3,2,2,1], 3))