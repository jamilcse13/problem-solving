class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dictS = {}
        a = 1
        
        for i in s:
            if i in dictS:
                dictS[i] = dictS[i]+1
            else:
                dictS[i] = a

        val = dictS[s[0]]
        for value in dictS.values():
            if val != value:
                return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)