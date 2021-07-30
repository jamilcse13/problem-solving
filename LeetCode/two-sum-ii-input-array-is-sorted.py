class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        length = len(numbers)
        
        for i in range(length):
            diff = target - numbers[i]
            if diff in hashMap:
                if i+1 < hashMap[diff]+1:
                    return [i+1, hashMap[diff]+1]
                else:
                    return [hashMap[diff]+1, i+1]
            hashMap[numbers[i]] = i
