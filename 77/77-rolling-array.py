class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
            
        f = [[0 for _ in range(len(B) + 1)] for _ in range(2)]
        pre, cur = 1, 0
        
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    f[cur][j] = max(f[cur][j], f[pre][j - 1] + 1)
                    
                else:
                    f[cur][j] = max(f[pre][j], f[cur][j - 1])
            
            pre, cur = cur, pre
                    
        return f[pre][-1]
        
        
