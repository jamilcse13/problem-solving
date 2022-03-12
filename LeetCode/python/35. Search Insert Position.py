class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        
        left = 0
        right = len(nums)-1
        
        if nums[right] < target:
            return right+1
        
        while left <= right:
            mid = (left + right)//2

            if nums[mid] < target:
                left=mid +1
            elif nums[mid] > target:
                right=mid -1
            else: 
                return mid
        return left

# Time Complexity: O(logn)
# Space Complexity: O(1)