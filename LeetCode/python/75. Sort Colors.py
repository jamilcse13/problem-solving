# Approach 1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        iterate = 0
        i = 0
        
        while length > iterate:
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
            else:
                i += 1
            iterate += 1

# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach 2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        iterate = 0
        zero = 0
        two = 0
        i = 0
        
        while length > iterate:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                if i == zero or nums[i] == 1:
                    i += 1
                zero += 1
            elif nums[i] == 2:
                ind = length - two - 1
                nums[ind], nums[i] = nums[i], nums[ind]
                two += 1
            else:
                i += 1
            
            iterate += 1

# Time Complexity: O(n)
# Space Complexity: O(1)