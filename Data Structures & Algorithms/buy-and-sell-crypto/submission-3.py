class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force = loop each day price as buy with following days as sell and check for max profit
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)

            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit




        


               