class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        end=len(numbers)-1
        
        while i < end:
            res = numbers[i] + numbers[end]
            if res == target:
                return [i+1, end+1]
            
            if res > target:
                end = end-1
                
            else:
                i += 1
            
        