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
def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    columns = len(matrix[0])
    
    for i in range(rows):
        for j in range(i, columns):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    
    for i in range(columns):
        for j in range(columns//2):
            temp = matrix[i][j] 
            matrix[i][j] = matrix[i][columns-1-j]
            matrix[i][columns-1-j] = temp