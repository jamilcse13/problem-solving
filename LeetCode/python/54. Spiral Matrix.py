class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        top = left = 0
        bottom = rows-1
        right = cols-1
        result = []
        port = 1
        
        while left<=right and top<=bottom:
            if port == 1:
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top += 1
                port = 2
                
            elif port == 2:
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                right -= 1
                port = 3
            
            elif port == 3:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
                port = 4
                
            elif port == 4:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
                port = 1
            
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)