class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        
        h1 = h2 = -max(prices) 
        s1 = s2 = 0 
        for index, price in enumerate(prices):
            s2 = max(s2, h2 + price)
            h2 = max(h2, s1 - price)
            
            s1 = max(s1, h1 + price)
            h1 = max(h1, -price)
        
        return max(s2, s1)