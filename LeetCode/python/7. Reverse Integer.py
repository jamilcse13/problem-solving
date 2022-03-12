class Solution:
    def reverse(self, x: int) -> int:
        b = 0
        y = abs(x)
        
        while int(y):
            a = int(y%10)
            y = y/10
            b = b*10 + a
        if x<0:
            return -b if int(b)<=2**31 else 0
        else:
            return b if int(b)<=2**31 else 0

# Time Complexity: O(length of x)
# Space Complexity: O(1)