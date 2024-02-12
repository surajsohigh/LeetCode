class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi = 0
        
        for i in prices:           
            mini = min(mini, i)
            profit = i - mini
            maxi = max(maxi, profit) # 4 5 
            
        return maxi