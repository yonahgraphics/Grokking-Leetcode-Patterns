#Fib sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...
# In general nth fib num = n-2th + n-1th
# Task: Write a function to return the nth fibonacci number
# E.g when n = 5, ans = 5; when n = 7, ans = 13
# Leetcode: https://leetcode.com/problems/fibonacci-number/


# Naive Approach
# Time Complexity: O(2^N), where N is the nth fib number
# The space complexity is N, since at max number of stack frames occupied
# by the function calls at any time is N

# When we analyze the space complexity of a recursive call, we have to include
# the additonal stack space that the functions calls take off the stack space
#Each of these calls is added to the call stack and takes
# up actual memory. So code like this would take O(n) auxiliary space.
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# Memoization: Caching the values we have already calculated so we don't calculate them again
# Memoizations reuses some values we already have and cuts the time complexity down.
# Time complexity: O(2N) === O(N), where N is the Nth fib number in the top-level call
# This is because the memo reduces the tree structure to just 2pairs per level.
# Space complexity: is still O(N)

# Using just one function
def fibOptimum1(n, memo = {}):
    if n in memo: # Base case1
            return memo[n]
    if n <= 2: # Base case2
        return 1
    memo[n] = fibOptimum1(n-1, memo) + fibOptimum1(n-2, memo)
    return memo[n]

# Using a helper function
# Memoization
def fibOptimum2(n):
    memo = {}
    return helper(n, memo)

def helper(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = helper(n-1, memo) + helper(n-2, memo)
    return memo[n]

# Class implementation
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]

def fibIterative(n):
    if n <= 2:
        return 1
    prev = 1
    past = 1
    for i in range(3, n+1):
        fib = past + prev
        past  = prev
        prev  = fib
    return fib


if __name__ == "__main__":
    # print(fib(50))
    print(fibOptimum1(0))
    # print(fibOptimum2(50))
    print(fibIterative(0))