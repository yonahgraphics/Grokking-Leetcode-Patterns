'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Leetcode Link: https://leetcode.com/problems/climbing-stairs/

'''

#Approach1: Recursion (DFS)
# Time Complexity: O(2^N) because we take 2 decisions at every step
# Spae complexity: O(h) == O(N). h == N is the height of the tree 
def climbStairs1(n):
    return helper(n)
def helper(n, memo = {}):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = helper(n-1, memo) + helper(n-2, memo)
    return memo[n]
    
# Approach 2: Iterative
# Time complexity: O(N)
# Space complexity: O(1)
def climbStairs2(n):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    Past = 1
    Prev = 1
    for i in range(2, n+1):
        num_ways = Past + Prev
        Past = Prev
        Prev = num_ways
    return num_ways

if __name__ == "__main__":
    print(climbStairs1(-1))
    print(climbStairs2(-1))