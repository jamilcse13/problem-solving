class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        length = len(keysPressed)
        ans = releaseTimes[0]
        ansCh = keysPressed[0]
        
        for i in range(1,length):
            t = releaseTimes[i] - releaseTimes[i - 1]
            if t > ans:
                ansCh = keysPressed[i]
                ans = t
            elif t == ans:
                ansCh = max(keysPressed[i], ansCh)
        return ansCh

# Time Complexity: O(n)
# Space Complexity: O(1)