class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sum1 = (l*(l+1))//2
        print(sum1)

        sum2 = sum(nums)
        print(sum2)

        if sum1 == sum2:
            return 0

        else:
            res = sum1-sum2

        return res

        
        