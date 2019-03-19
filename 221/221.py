class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix or not matrix[0]:
            return 0
        
        f = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        ans = 0
        for i in range(len(matrix)):
            row_count = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0":
                    continue
                    
                row_len = f[i][j - 1] + 1 if j > 0 else 1
                col_len = f[i - 1][j] + 1 if i > 0 else 1
                
                f[i][j] = min(col_len, row_len)
                if i > 0 and j > 0:
                    f[i][j] = min(f[i - 1][j - 1] + 1, f[i][j])
                ans = max(ans, f[i][j])
                
        return ans * ans
                    
                
                    
            
        