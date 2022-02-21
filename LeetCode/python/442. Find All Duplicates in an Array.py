class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        hashMap = {}
        
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
                
        nums.clear()
        
        for key, value in hashMap.items():
            if value == 2:
                nums.append(key)
                
        return nums

# Time Complexity: O(n)
# Space Complexity: O(n)