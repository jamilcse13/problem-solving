class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        length = len(nums)
        nums_set = {}
        count = 0
        
        for i in nums:
            if i in nums_set:
                nums_set[i] += 1
            else:
                nums_set[i] = 1
        
        
        for num, counts in nums_set.items():
            if k == 0:
                if counts >= 2:
                    count += 1
            else:
                if (num-k) in nums_set:
                    count += 1
                    
        return count
        
# Time Complexity: O(n)
# Space Complexity: O(n)