class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        val = defaultdict(int)
        
        for i, j in enumerate(nums):
            val[j] += 1 
        
        for key, value in val.items():
            print(key, value)
            if value >= 2 :
                return key
            
                
        
        
        
        
        # a=Counter(nums).most_common()
        # print(a)
        # return a[0][0]
        
        
#         Simple Approach, Except [2,2,2,2,2]
#         num1 = sum(set(nums))
#         num2 = sum(nums)
        
#         return num2-num1
        