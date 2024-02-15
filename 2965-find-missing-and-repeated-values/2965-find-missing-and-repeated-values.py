class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        size = len(grid[0])
        n = size*size
        
        dic=[]
        for i in grid:
            for idx, j in enumerate(i):
                dic.append(j)
        
        res2 = Counter(dic).most_common()[0][0]
         
                
                
        data1 = n*(n+1)//2
        data2 = sum(set(dic))
        res1 = data1-data2
        
        
                
        return [res2, res1]
        
        