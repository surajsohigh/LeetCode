class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m=len(matrix) # col
        n=len(matrix[0]) # row
        
        row = [0] * n
        col = [0] * m
        
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    col[i] = 1
                    row[j] = 1
                    
        for i in range(m):
            for j in range(n):
                if col[i] or row[j]:
                    matrix[i][j] = 0
                    
                    
        return matrix
        print (row)
        print (col)        