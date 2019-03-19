class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix or not matrix[0]:
            return 0
        
        f = [[0 for _ in range(len(matrix[0]))] for _ in range(2)]
        pre, cur = 1, 0
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0":
                    f[cur][j] = 0
                    continue
                    
                row_len = f[cur][j - 1] + 1 if j > 0 else 1
                col_len = f[pre][j] + 1 if i > 0 else 1
                
                f[cur][j] = min(col_len, row_len)
                if i > 0 and j > 0:
                    f[cur][j] = min(f[pre][j - 1] + 1, f[cur][j])
                
                ans = max(ans, f[cur][j])
            
            pre, cur = cur, pre
                
        return ans * ans
                    
                
                    
            
        