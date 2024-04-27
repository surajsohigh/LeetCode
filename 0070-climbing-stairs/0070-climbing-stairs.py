class Solution:
    def climbStairs(self, n: int) -> int:
        
        one=1
        two=1
        
        for i in range(n-1):
            res = one+two
            two = one
            one = res
            
            
        return one
            
        