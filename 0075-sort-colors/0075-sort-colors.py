class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        two=0
        
        
        for i in range (0, len(nums)):
            if 2 == nums[i]:
                two = two + 1
            elif 1 == nums[i]:
                one = one + 1
            else:
                zero = zero + 1
        
        
        for i in range(0, len(nums)):
            if zero:
                nums[i]=0
                zero = zero-1
            elif one:
                nums[i]=1
                one = one-1
            else: 
                nums[i]=2
                two = two-1
        print(zero, one, two)
        print(nums)
                       