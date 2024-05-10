class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        for i in range(len(s)):

            string = ""
            for j in range(i, len(s)):
                if s[j] not in string:
                    string += s[j]
                else:
                    break
            maxi = max(maxi, len(string))
            print(i, string)
            
        return maxi
                
            