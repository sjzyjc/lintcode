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
            
        f = [False for _ in range(m + 1)]
        f[0]= True
        prefix_sum = 0
        
        for i in range(1, len(A) + 1):
            prefix_sum += A[i - 1]
            
            for j in range(min(prefix_sum, m), A[i - 1] - 1, -1):
                f[j] = f[j] or f[j - A[i -1]]
                    
        for i in range(m, -1, -1):
            if f[i]:
                return i
                
        return 0
            