class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        string = s.split(" ")[-1]
        print(string)
        return len(string)





