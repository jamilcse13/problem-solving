class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return True if len(nums) != len(list(set(nums))) else False       //One line solution
        
        hashMap = {}
        
        for i in nums:
            if i in hashMap:
                return True
            hashMap[i] = 1
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)