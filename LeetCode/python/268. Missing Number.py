class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summation = 0
        maxNum = len(nums)
        totalSum = (maxNum*(maxNum+1))/2
        
        for i in nums:
            summation += i
        return int(totalSum - summation)

# Time Complexity: O(n)
# Space Complexity: O(1)
