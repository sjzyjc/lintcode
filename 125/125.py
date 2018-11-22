class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if not A or not V:
            return 0
            
        if m <= 0:
            return 0
            
        f = [-1 for _ in range(m + 1)]
        f[0] = 0
        
        for i in range(1, len(A) + 1):
            for w in range(m, A[i - 1] - 1, -1):
                if f[w - A[i - 1]] == -1:
                    continue 
                
                f[w] = max(f[w], f[w - A[i - 1]] + V[i - 1])
        
        return max(f)