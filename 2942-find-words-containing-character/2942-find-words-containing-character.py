class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ar = []
        for idx, i in enumerate(words):
            if x in i:
                # print("yes", idx, i)
                ar.append(idx)
                
        print(ar)
        return ar