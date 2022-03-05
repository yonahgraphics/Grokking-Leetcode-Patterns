'''
N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Leetcode link: https://leetcode.com/problems/n-th-tribonacci-number/
'''
# Approach1: Recursion
# Time Complexity: O(n^3), because we take 3 decisions at every step
# Space Complexity: O(h) == O(n) 
def tribonacci1(n):
    return helper(n)
def helper(n, memo = {}):
    if n == 0 or n < 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = helper(n-1, memo) + helper(n-2, memo) + helper(n-3, memo) 
    return memo[n]

# Approach1: Iterative
# Time complexity: O(N)
# Space complexity: O(1)
def tribonacci2(n):
    if n == 0 or n < 0:
        return 0
    if n == 1 or n == 2:
        return 1
    first, second, third = 0, 1, 1
    
    for i in range(3, n+1):
        trib = first + second + third
        first = second
        second = third
        third = trib
    return trib

if __name__ == "__main__":
    print(tribonacci1(90))
    print(tribonacci2(90))