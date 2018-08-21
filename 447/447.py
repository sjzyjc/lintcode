class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 1
        while reader.get(index) < target:
            index = index * 2
        
        start, end = 0, index

        while start < end:
            mid = start + (end - start) // 2
            
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) < target:
                start = mid + 1
            else:
                end = mid - 1 
        
        if reader.get(start) == target:
            return start
        
        return -1  