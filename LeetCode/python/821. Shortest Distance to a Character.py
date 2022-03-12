class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        length = len(s)
        ans = []
        index = []
        
        for i in range(length):
            if (s[i] == c):
                index.append(i)
        
        for i in range(length):
            # ans.append(min(abs(i-index[0]), abs(i-index[1])))
            ans.append(min(abs(i-id) for id in index))
            
        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)