class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = "false"
        for i in range(len(nums)):
            if nums[i] >= target:
                falg="true"
                return i
            
        if flag == "false":
            return len(nums)
            
                