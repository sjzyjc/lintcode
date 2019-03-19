"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
            
        arr = []
        for p in airplanes:
            arr.append((p.start, 1))
            arr.append((p.end, 0))
        
        arr.sort()
        ans = 0
        count = 0
        for i in arr:
            if i[1] == 1:
                count += 1
            else:
                count -= 1
                
            ans = max(ans, count)
            
        return ans
                
        
