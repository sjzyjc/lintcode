class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
            
        if k > len(pages):
            return min(pages)
            
        f = [[(1 << 31) - 1 for _ in range(k + 1)] for _ in range(len(pages) + 1)]
        f[0][0] = 0
        
        #print(f)
        for i in range(1, len(pages) + 1):
            for j in range(1, k + 1):
                copy_time = 0
                f[i][j] = f[i][j - 1]
                for sub in range(i - 1, -1, -1):
                    copy_time += pages[sub]
                    
                    if copy_time > f[i][j]:
                        break
                    
                    total = max(f[sub][j - 1], copy_time)    
                    f[i][j] = min(f[i][j], total)
                    
        return f[-1][-1]
                
