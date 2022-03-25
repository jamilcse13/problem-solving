from typing import List

class Solution:
    @classmethod
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        arr = []

        if m*n != length:
            return arr
        
        for i in range(0, length, n):
            arr.append(original[i:i+n])
        
        return arr

# Time Complexity: O(n)
# Space Complexity: O(m*n)