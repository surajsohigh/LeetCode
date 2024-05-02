from collections import deque

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        dup=len(nums)-1
        left=len(nums)-1
        
        while left >= 0:
            if nums[left] == val:
                print("h")
                nums[dup], nums[left] = nums[left], nums[dup]
                dup -= 1
                
            
            left -= 1
            
        
        numDup = len(nums[:dup+1])
        print(nums, dup, numDup)
        return numDup
        
        
        
            
            
        
        