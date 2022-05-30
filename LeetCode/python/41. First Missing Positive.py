class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1

        for num in nums:
            num = abs(num)
            if num - 1 < length:
                nums[num-1] = abs(nums[num-1]) * -1
        
        for i in range(length):
            if nums[i] > 0:
                return i+1
        
        return length+1


# Time Complexity: O(n)
# Space Complexity: O(1)