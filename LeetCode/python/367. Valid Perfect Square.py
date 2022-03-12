class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        assumeNum = num/2
        
        while True:
            temp = assumeNum
            assumeNum = (temp + (num/temp))/2
            
            if temp == assumeNum:
                if temp-int(temp) == 0.0:
                    return True
                return False

# Time Complexity: O(logn)
# Space Complexity: O(1)
