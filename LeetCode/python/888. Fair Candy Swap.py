class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        box = set(bobSizes)
        
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        candy = int((alice + bob)/2)
        

        for i in aliceSizes:
            a = candy - alice
            aliceNeed = a+i
            
            if aliceNeed in box:
                return [i,aliceNeed]

# Time Complexity: O(n)
# Space Complexity: O(1)