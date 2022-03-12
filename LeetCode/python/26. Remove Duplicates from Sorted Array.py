class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashMap = {}
        length = len(nums)
        count = 0
        
        for i in range(length):
            if not nums[i] in hashMap:
                hashMap[nums[i]] = i
                nums[count] = nums[i]
                count += 1
        return count

# Time Complexity: O(n)
# Space Complexity: O(n)
