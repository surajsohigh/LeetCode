class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        # init = nums[0]
        for i in range(len(nums)):
            if x == 0 or x == 1:
                if nums[i]>=nums[i-1]:
                    pass
                else:
                    x += 1

        if x == 0 or x == 1:
            return True
        else:
            return False