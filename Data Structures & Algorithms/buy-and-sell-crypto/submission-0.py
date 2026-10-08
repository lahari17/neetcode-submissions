class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for buy in range(len(prices)-1):
            for sell in range(buy+1, len(prices)):
                if prices[sell]>prices[buy]:
                    if (prices[sell]-prices[buy])>profit:
                        profit=prices[sell]-prices[buy]
                    
        return profit

#Time-O(n2)
#Space-O(1)