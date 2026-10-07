class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy = prices[0]    
        profit = 0

        for i in prices:
            if i < buy:
                buy = i
            else:
                final = i - buy
                if profit < final:
                    profit = final

        return profit
            
        