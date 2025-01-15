class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 0

        if not nums:
            return 0

        while end < len(nums):
            if nums[start] != nums[end]:
                start += 1
                nums[start] = nums[end]

            end += 1
        print(nums)

        return start+1

