'''
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to
modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Leetcode Link: https://leetcode.com/problems/rotate-image/
'''

'''
Complexity Analysis
--------------------
Time Complexity: O(R * C), where R and C are the number of rows and columns in the given matrix A.
Space Complexity: O(1), b'se we don't use extra space.
'''
def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # Transpose the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(i, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
    # Then reverse it
    for i in range(cols):
        l, r = 0, len(matrix[i])-1
        while l < r:
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1