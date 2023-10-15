class Solution:
    def reverse(self, x: int) -> int:
        st=0
        num=abs(x)
        for i in range(0, len(str(num))):
            q=num//10
            r=num%10
            st=st*10+r
            num=q

        if st > 2**31:
            return 0
        if x < 0:
            # print(st)
            st = st*-1
            return st
        else: 
            return st



