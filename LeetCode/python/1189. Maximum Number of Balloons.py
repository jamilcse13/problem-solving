class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ball = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        
        for i in text:
            if i in ball:
                ball[i] += 1
        ans = min(ball['b'], ball['a'], ball['l']//2, ball['o']//2, ball["n"])
        return ans

# Time Complexity: O(n)
# Space Complexity: O(1)