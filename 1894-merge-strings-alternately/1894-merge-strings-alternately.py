class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        li1 = [*word1]
        li2 = [*word2]
        for i, j in zip(li1, li2):
            s = s+i+j
        
        size = min(len(li1), len(li2))
        s += word1[size:] + word2[size:]

        
        return s