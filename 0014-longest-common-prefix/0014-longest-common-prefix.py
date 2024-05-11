class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        
        print(strs)
        arrSize = len(strs)
        
        minlen = min(len(strs[0]), len(strs[arrSize-1]))
        
        print(minlen)
        
        i=0
        string = ""
        while i < minlen and strs[0][i] == strs[arrSize-1][i]:
            string += strs[0][i]
            i = i+1
            
        print(string)
        return string
        
        
        
        
        