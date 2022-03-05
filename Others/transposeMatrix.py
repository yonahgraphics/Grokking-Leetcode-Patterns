'''
Complexity Analysis
--------------------
Time Complexity: O(R * C), where RR and CC are the number of rows and columns in the given matrix A.
Space Complexity: O(R * C), the space used by the answer.
'''

def transpose(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    columns = len(matrix[0])
    
    # Create a result matrix of zeros
    # By looping over the columns and the rows nested
    new_matrix = []
    for i in range(columns):
        new_matrix.append([]) # Append as many rows as there is columns in the original matrix
        for j in range(rows):
            new_matrix[i].append([0]) # Append as many zeros as there is rows in each inner list
    
    # Now replace the zeros with the numbers
    for i in range(rows):
        for j in range(columns):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

# Alternative way of creating a result matrix
def transpose1(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    columns = len(matrix[0])
    
    # Create a result matrix of zeros
    # By looping over the columns and the rows nested
    new_matrix = []
    for i in range(columns):
            new_matrix.append(rows*[0]) # Append as many zeros as there is rows in each inner list
    
    # Now replace the zeros with the numbers
    for i in range(rows):
        for j in range(columns):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

if __name__ == "__main__":
    matrix =    [
                [1,2,3],
                [4,5,6]
                ]
    print("Original Matrix", matrix)
    print("Transposed Matrix", transpose1(matrix))
        