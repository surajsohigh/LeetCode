class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumofNumber(n)
            
            if n == 1:
                return True
            
        return False
        
    
    def sumofNumber(self, n:int):
        digit = 0
        while n:
            remainder = n % 10 
            remainder = remainder ** 2
            digit += remainder
            n = n // 10
            
        return digit

            