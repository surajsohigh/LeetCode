class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start = 0
        end = 1
        maxp  = 0
        
        while end < len(prices):
            if prices[start] < prices[end]:
                res = prices[end] - prices[start]
                maxp = max(res, maxp)
                
            else:
                start=end

            end += 1
        return maxp
