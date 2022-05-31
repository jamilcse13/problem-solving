class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_substrings = set()
        length = len(s)
        
        for i in range(length - k + 1):
            all_substrings.add(s[i:i+k])
        
        return len(all_substrings) == 1 << k

# Time Complexity: O(n/k)
# Space Complexity: O(2^k)