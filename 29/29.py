class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if ((not s1) and (not s2)) == (not s3) == True:
            return True
        
        if (s1 is not None or s2 is not None) and s3 is None:
            return False
            
        if len(s1) + len(s2) != len(s3):
            return False
            
        f = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        f[0][0] = True
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i + j - 1 >= 0 and i - 1 >= 0 and s3[i + j - 1] == s1[i - 1]:
                    f[i][j] = f[i][j] or f[i - 1][j]
                
                if i + j - 1 >= 0 and j - 1 >= 0 and s3[i + j - 1]  == s2[j - 1]:
                    f[i][j] = f[i][j] or f[i][j - 1]
                    
        return f[-1][-1]