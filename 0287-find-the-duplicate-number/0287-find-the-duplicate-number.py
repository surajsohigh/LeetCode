class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=Counter(nums).most_common()
        return a[0][0]
        
        
#         Simple Approach, Except [2,2,2,2,2]
#         num1 = sum(set(nums))
#         num2 = sum(nums)
        
#         return num2-num1
        