class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        
        if not A or not V or m <= 0:
            return 0
            
        f = [-1 for _ in range(m + 1)]
        f[0] = 0
        
        for i in range(1, len(A) + 1):
            for w in range(m + 1):
                if w < A[i - 1] or f[w - A[i - 1]] == -1:
                    continue
                
                f[w] = max(f[w - A[i - 1]] + V[i - 1], f[w])
        
        return max(f)
