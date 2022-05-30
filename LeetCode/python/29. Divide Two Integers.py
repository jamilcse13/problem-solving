class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        count = 0
        flag  = 0
        if (dividend < 0) == (divisor < 0):
            flag = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
            
        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                count += 1 << i
        
        return -count if flag == 0 else count


# Time Complexity:
# Space Complexity: O(1)