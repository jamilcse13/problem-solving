class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        
        if length == 1:
            return 0
        
        for i in range(1, length):
            if nums[i-1] >= nums[i]:
                temp = nums[i-1] - nums[i]
                nums[i] = nums[i]+temp+1
                count += temp+1
            
        return count

# Time Complexity: O(n)
# Space Complexity: O(1)
