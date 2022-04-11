"""
Leetcode: https://leetcode.com/problems/shift-2d-grid/
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
"""
def shiftGrid(self, grid, k):
    
    nrows = len(grid)
    ncols = len(grid[0])
    
    res = []
    for _ in range(nrows):
        res.append([0]*ncols)
    
    for r in range(nrows):
        for c in range(ncols):
            shiftedIndex = ((r*ncols+c)+k) % (nrows*ncols)
            newRow, newCol = shiftedIndex//ncols, shiftedIndex%ncols
            res[newRow][newCol] = grid[r][c]
    return res
        