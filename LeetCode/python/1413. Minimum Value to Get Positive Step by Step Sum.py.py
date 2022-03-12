class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        a = nums[0]
        b = 0
        
        for i in range (0, len(nums)):
            b = b + nums[i]
            if a > b:
                a = b
            
        if a<0:
            return abs(a)+1    
        else:
            return 1

# Time Complexity: O(n)
# Space Complexity: O(1)