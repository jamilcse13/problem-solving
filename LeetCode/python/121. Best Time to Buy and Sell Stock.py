class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        bestProfit = 0
        
        for i in prices:
            profit = i-low
            if profit > bestProfit:
                bestProfit = profit
            elif i < low:
                low = i
        return bestProfit


# Time Complexity: O(n)
# Space Complexity: O(1)