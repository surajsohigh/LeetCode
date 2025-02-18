class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        di = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        di_val = di.values()
        if len(set(di_val)) == 1:
            return True
        else:
            return False
        