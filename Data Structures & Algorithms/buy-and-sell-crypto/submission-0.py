class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = prices[0]
        profit = 0
        for num in prices:
            mp = min(mp, num)
            profit = max(profit, num-mp)
        return profit