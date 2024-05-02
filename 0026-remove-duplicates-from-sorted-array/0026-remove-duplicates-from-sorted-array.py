class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        left=0
        right=0
        length = len(nums)
        
        while right < length:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
                
            right += 1
            
        left = left + 1
        unique = len(nums[:left])
        print(unique, nums[:left])
            
        return unique