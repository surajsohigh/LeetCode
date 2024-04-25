class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i=0;j=1
        maxp = 0
        siz=len(prices)
        while j < siz: 
            if prices[i] < prices[j]:
                res = prices[j] - prices[i]
                if res > maxp:
                    maxp=res   
            else:
                # i=i+1 or we can say that
                i=j
                
            j=j+1
            
        return maxp
                
                
                
            
        