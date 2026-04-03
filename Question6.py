# Write a Python program to compute the determinant of a square matrix manually.
def minors(matrix, i, j):
    
    # Creating a new matrix by slicing the original matrix, excluding row 'i' and column 'j'
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def matrixdeterminant(matrix):
    
    n = len(matrix)
    
    # Base case for a 1x1 matrix
    
    if n == 1:
        return matrix[0][0]
    
    # Base case for a 2x2 matrix
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # for matrices larger than 2x2
    
    determinant = 0

    for j in range(n):
        
        # Calculating the minor for element matrix[0][j]

        minor = minors(matrix, 0, j)
        
        # Determining the sign based on the column index (j)

        sign = (-1) ** j
        
        # Adding to the total determinant

        determinant = determinant + (sign * matrix[0][j] * matrixdeterminant(minor))
        
    return determinant

matrix1= [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
det1= matrixdeterminant(matrix1)
print(f"The determinant of the 3x3 matrix is: {det1}")