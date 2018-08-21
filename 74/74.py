class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        
        if n is None or n < 1:
            return -1
        
        start, end  = 1, n
        while start < end:
            mid =  start + (end - start) // 2
            
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
            
        if SVNRepo.isBadVersion(start):
            return start
        
        return -1 
            