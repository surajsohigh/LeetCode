class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arrHash1 = {}
        arrHash2 = {}

        for i in range(len(s)):
            arrHash1[s[i]] = 1 + arrHash1.get(s[i], 0)
            arrHash2[t[i]] = 1 + arrHash2.get(t[i], 0)
            
        print(arrHash1, arrHash2)

        for i in arrHash1:
            print(i)
            if arrHash1[i] != arrHash2.get(i, 0):
                return False

        return True


        