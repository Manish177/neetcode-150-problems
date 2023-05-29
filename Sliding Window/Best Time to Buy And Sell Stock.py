class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        start=prices[0]
        profit=0

        for i in prices[1:]:
            if i < start:
                start=i
            else:
                profit=i-start         
            max_profit=max(max_profit, profit)
        return max_profit