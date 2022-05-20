class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hashSet = set()
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    hashSet.add(('r', i))
                    hashSet.add(('c', j))
        
        for el in hashSet:
            col, ind = el
            for i in range(r):
                for j in range(c):
                    if (col == 'r' and i == ind) or (col == 'c' and j == ind):
                        matrix[i][j] = 0


# Time Complexity: O(m*n)
# Space Complexity: O(m+n)



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hashMap = {}
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    hashMap['r-'+str(i)] = 0
                    hashMap['c-'+str(j)] = 0
        
        for el in hashMap:
            for i in range(r):
                    for j in range(c):
                        if (el.split('-')[0] == 'r' and i == int(el.split('-')[1])) or (el.split('-')[0] == 'c' and j == int(el.split('-')[1])):
                            matrix[i][j] = 0


# Time Complexity: O(m*n)
# Space Complexity: O(m*n)