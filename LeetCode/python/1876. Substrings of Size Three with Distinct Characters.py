class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        
        for i in range(length-2):
            if len(s[i:i+3]) == len(set(s[i:i+3])):
                count += 1
                
        return count

# Time Complexity: O(n)
# Space Complexity: O(1)