class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasTable = {}
        for idx, dig in enumerate(nums):
            diff = target-dig 
            if diff in hasTable:
                return [idx, hasTable[diff]]
            
            hasTable[dig] = idx
        