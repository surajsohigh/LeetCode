class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        for i in nums:
            if currsum < 0:
                currsum = 0
            currsum += i
            maxsum = max(maxsum, currsum)
            
        return maxsum
        