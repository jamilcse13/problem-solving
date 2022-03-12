class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = ''
        count = 0
        
        for lt in word:
            if lt == ch:
                arr = lt + arr
                count += 1
                break
            else:
                arr = lt + arr
        return arr+word[len(arr):] if count > 0 else word

# Time Complexity: O(n)
# Space Complexity: O(1)