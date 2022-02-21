# using loop
class Solution:
    def addDigits(self, num: int) -> int:        
        sum = 0
        
        if num <= 9:
            return num
        else:
            while num>=1:
                sum += num%10
                num = int(num/10)
                if num==0 and sum>9:
                    num = sum
                    sum = 0
            return sum

# Time Complexity: O(1)
# Space Complexity: O(1)


# Optimal solution with using loop and space
class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        elif num%9 == 0:
            return 9
        else:
            return num%9

# Time Complexity: O(n)
# Space Complexity: O(1)
s = Solution()
s.addDigits(1234)