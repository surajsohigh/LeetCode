class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        sarr1 = m 
        sarr2 = n 
        last = (m+n)-1 
        
        while sarr2 > 0 and sarr1 > 0:
            
            if nums1[sarr1-1] > nums2[sarr2-1]:
                nums1[last] = nums1[sarr1-1]
                sarr1 -= 1
                
            else:
                nums1[last] = nums2[sarr2-1]
                sarr2 -= 1
            last -= 1
            print(nums1, last)
        
        while sarr2 > 0:
            nums1[last] = nums2[sarr2-1]
            last -= 1
            sarr2 -= 1
                
       
        # i=0; j=0
#         li = nums1[:m]
#         idx = 0
#         while i<n and j<m:
#             if li[i] < nums2[j]:
#                 nums1[idx]=li[i]
#                 idx=idx+1
#                 i=i+1
#             else:
#                 nums1[idx]=nums2[j]
#                 idx=idx+1
#                 j=j+1
                
#         if i == len(li) 
                
#         while i < len(li):
#             nums1[idx] = li[i]
#             idx = idx+1
#             i=i+1
            
#         while j < len(nums2):
#             nums1[idx] = nums2[j]
#             idx = idx+1
#             j=j+1
        
        


#         print(nums1)
        
        
            
        
            
            