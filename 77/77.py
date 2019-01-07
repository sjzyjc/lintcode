class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    O(MN)
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
            
        f = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
                    
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
                    
                    
        return f[-1][-1]
        
        
