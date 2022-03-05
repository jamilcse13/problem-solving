class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(col-1):
            for j in range(row-1):
                matrix[i][j] = matrix[row-1-j][i]

# Time Complexity: O(m*n)
# Space Complexity: O(1)