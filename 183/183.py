class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if k <= 0 or k > sum(L) or not L:
            return -1
            
        start = 1
        end = max(L)
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.compute(mid, L) >= k:
                start = mid
                
            else:
                end = mid - 1
                
        if self.compute(end, L) >= k:
            return end
            
        return start
        
    def compute(self, length, L):
        total = 0
        for item in L:
            total += item // length
            
        return total
        
