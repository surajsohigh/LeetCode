class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxNum=nums[0]
        
        for i in nums:
            sum = sum + i
            maxNum = max(sum, maxNum)
            
            if sum < 0:
                sum=0
                
        return maxNum
        