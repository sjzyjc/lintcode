class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        if not prices:
            return 0
            
        if k > len(prices) // 2:
            ans = 0
            for index in range(1, len(prices)):
                if prices[index] > prices[index - 1]:
                    ans += prices[index] - prices[index - 1]
                    
            return ans
        
        max_price = max(prices)
        h = [-max_price for _ in range(k)]
        s = [0 for _ in range(k)]
        
        for price in prices:
            for i in range(k - 1, -1, -1):
                s[i] = max(s[i], h[i] + price)
                
                if i > 0:
                    h[i] = max(h[i], s[i - 1] - price)
                else:
                    h[i] = max(h[i], -price)
                
        return max(s)
                