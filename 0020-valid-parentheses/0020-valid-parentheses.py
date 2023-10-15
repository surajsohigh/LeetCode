class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        dic = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in dic:
                if lis and lis[-1] == dic[i]:
                    lis.pop()
                else:
                    return False
            else:
                lis.append(i)

        return False if lis else True


        return True
