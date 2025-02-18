class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newString = s.strip()
        newString = newString.split(" ")
        return len(newString[-1])
        # print()

        