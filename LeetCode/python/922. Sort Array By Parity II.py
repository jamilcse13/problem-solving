class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        length = len(nums)
        oddNum = []
        evenNum = []
        ans = []
        
        for i in range(length):
            if nums[i]%2 == 0:
                evenNum.append(nums[i])
            else:
                oddNum.append(nums[i])
                
        indOdd=0
        idEven=0
        
        for i in range(length):
            if i%2 == 0:
                nums[i] = evenNum[idEven]
                idEven += 1
            else:
                nums[i] = oddNum[indOdd]
                indOdd += 1
            
        return nums

# Time Complexity: O(n)
# Space Complexity: O(n)