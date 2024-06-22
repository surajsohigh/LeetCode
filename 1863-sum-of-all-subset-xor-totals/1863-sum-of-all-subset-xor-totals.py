from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Iterate over all possible subsets
        for i in range(1 << n):  # 2^n subsets
            subset_xor = 0
            for j in range(n):
                if i & (1 << j):  # Check if j-th element is included in the subset
                    subset_xor ^= nums[j]
            total_sum += subset_xor
        
        return total_sum

# Example usage
solution = Solution()
print(solution.subsetXORSum([5,1,6]))  # Output: 28
