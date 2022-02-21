class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        hashMap = {}
        
        for i in nums:
            hashMap[i] = 1
        
        nums.clear()
                
        for i in range(1,length+1):
            if i not in hashMap:
                nums.append(i)
        
        return nums

# Time Complexity: O(n)
# Space Complexity: O(n)