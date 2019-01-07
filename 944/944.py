class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return None
        
        ans = -(1 << 31)
        prefix_sum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j - 1 >= 0:
                    prefix_sum[i][j] += prefix_sum[i][j - 1]
                    
                if i - 1 >= 0:
                    prefix_sum[i][j] += prefix_sum[i - 1][j]
                    
                if j - 1 >= 0 and i - 1 >= 0:
                    prefix_sum[i][j] -= prefix_sum[i -1][j - 1]
                    
                prefix_sum[i][j] += matrix[i][j]
                
        for upper in range(len(matrix)):
            for lower in range(upper, len(matrix)):
                pre_min = 0
                
                for i in range(len(matrix[0])):
                    cur = prefix_sum[lower][i]
                    if upper - 1 >= 0:
                        cur -= prefix_sum[upper][i]
                    
                    ans = max(cur - pre_min, ans)
                    pre_min = min(pre_min, cur)
        
        return ans

sl = Solution()
a = [[1,3,-1],[2,3,-2],[-1,-2,-3]]
print(sl.maxSubmatrix(a))