class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        length = len(s)
        s_val = t_val = 0
        
        for i in range(length):
            s_val += ord(s[i])
            t_val += ord(t[i])
        t_val +=  ord(t[length])

        return chr(t_val-s_val)

# Time Complexity: O(n)
# Space Complexity: O(1)