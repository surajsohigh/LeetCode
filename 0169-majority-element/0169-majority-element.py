class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = {}

        for i in nums:
            if i in di:
                di[i] += 1
            
            else:
                di[i] = 1
        print(di, max(di, key=di.get))
        return max(di, key=di.get)

        # max(stats, key=stats.get)


        