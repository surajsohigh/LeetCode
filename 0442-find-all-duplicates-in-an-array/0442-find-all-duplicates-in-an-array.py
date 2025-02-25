class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        di = {}
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        li = []
        for i, j in di.items():
            if j > 1:
                li.append(i)

        print(li)
        return li
        