class Solution:
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        
        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp
            
            li += 1
            ri -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0 : 
            k += len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);


# class Solution:
    
#     def rev(self, nums, i, j):
#         print(i,j)
        
#         while (i < j):
#             nums[i], nums[j] = nums[j], nums[i]
#             i= i+1
#             j=j-1
            
#         # print(num)
#         return nums
        
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         if k < 0 : 
#             k += len(nums)
        
#         print(self.rev(nums, 0, k))
#         print(self.rev(nums, k+1, len(nums)-1))
#         print(self.rev(nums, 0, len(nums)-1))
        
#         return nums
        
        