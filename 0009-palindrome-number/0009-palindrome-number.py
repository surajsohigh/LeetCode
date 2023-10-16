class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sum = 0
        num=x
        while num > 0:
            q = num//10
            r = num%10
            sum = sum*10+r
            num = q

        print(sum)
        if sum == x:
            return True
        else:
            False
