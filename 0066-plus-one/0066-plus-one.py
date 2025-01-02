class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ''
        for i in digits:
            st += str(i)
        temp = str(int(st)+1)

        return [int(x) for x in str(temp)]
            