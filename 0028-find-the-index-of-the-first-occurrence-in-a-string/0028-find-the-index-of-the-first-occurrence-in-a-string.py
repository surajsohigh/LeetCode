class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack - needle make 
        size = len(haystack) - len(needle) + 1

        for i in range(size):
            if haystack[i: i+len(needle)] == needle:
                return i
            
        return -1