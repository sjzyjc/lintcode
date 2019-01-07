class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        if not A:
            return 0
            
        f = [[False for _ in range(m + 1)] for _ in range(len(A) + 1)]
        f[0][0] = True
        
        for i in range(1, len(A) + 1):
            for j in range(m + 1):
                f[i][j] = f[i - 1][j]
                
                if j >= A[i - 1]:
                    f[i][j] = f[i][j] or f[i - 1][j - A[i -1]]
                    
        for i in range(m, -1, -1):
            if f[-1][i]:
                return i
                
        return 0
            