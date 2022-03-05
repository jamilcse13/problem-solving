class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        length = len(nums)
        
        for i in range(length):
            diff = target - nums[i]
            if diff in hashMap:
                return [i, hashMap[diff]]
            hashMap[nums[i]] = i

# Time Complexity: O(n)
# Space Complexity: O(n)