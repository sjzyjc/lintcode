"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        
        if not list1:
            return list2
            
        if not list2:
            return list1
            
        ptr1, ptr2 = 0, 0
        ans = []
        last = Interval(- (1 << 31), - (1 << 31))
        
        while ptr1 < len(list1) and ptr2 < len(list2):
            int1 = list1[ptr1]
            int2 = list2[ptr2]
            min_int = None
            
            #get next min
            if int1.start < int2.start:
                min_int = int1
                ptr1 += 1
            else:
                min_int = int2
                ptr2 += 1
            
            self.append_last(ans, last, min_int)
                
        while ptr1 < len(list1):
            self.append_last(ans, last, list1[ptr1])
            ptr1 += 1
            
        while ptr2 < len(list2):
            self.append_last(ans, last, list2[ptr2])
            ptr2 += 1
        
        ans.append(last)    
        return ans[1:]
        
    def append_last(self, ans, last, min_int):
        if min_int.start > last.end:
            ans.append(Interval(last.start, last.end))
            last.start = min_int.start
            last.end = min_int.end
        else:
            last.start = min(last.start, min_int.start)
            last.end = max(last.end, min_int.end)
