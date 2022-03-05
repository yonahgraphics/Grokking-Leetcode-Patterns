# Given an n by m grid, return the number of ways you can travel from the
# topleft to the bottom right
# YOU CAN NOT TRAVEL DIAGONALLY
# E.g gridTraveller(2,3)---->3
# Leetcode: https://leetcode.com/problems/unique-paths/

# Brute-force
#Time complexity:  O(2^m+n)
#Space complexity: O(m+n)
def gridTraveller(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return gridTraveller(m-1, n) + gridTraveller(m, n-1)

# Optimum
# Time complexity: O(m*n). This is b'se distinct nodes for m and n after memoization are
# m = {0,1,2,.....,m}
# n = {0,1,2,.....,n}
# Some distinct nodes = m*n, which correspons to function calls
# Space complexity: O(m + n), ==== height of the tree
def gridTravellerOptimum(m, n, memo = {}):
    #Memoize and reduce duplicate work
    key = str(m) + "_"+ str(n)
    if key in memo:
        return memo[key]
    
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    memo[key] = gridTravellerOptimum(m-1, n, memo) + gridTravellerOptimum(m, n-1, memo)
    return memo[key]

# Class Implementation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.helper(m, n, memo)
    
    def helper(self, m, n, memo):
        key = str(m) + "_" + str(n)
        if key in memo:
            return memo[key]
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        memo[key] = self.helper(m-1, n , memo) + self.helper(m, n-1, memo)
        return memo[key]
        



if __name__ == "__main__":
    print(gridTravellerOptimum(18, 18))
    