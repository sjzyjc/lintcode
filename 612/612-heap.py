"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    nlogk + klogk
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        if not origin or not points or k < 0:
            return []
            
        heap = []
        for point in points:
            distance = self.getDistance(point, origin)
            heapq.heappush(heap, (-distance, -point.x, -point.y))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while len(heap) > 0:
            _, a, b = heapq.heappop(heap)
            ans.append(Point(-a, -b))
            
        return ans[::-1]
        
    
    def getDistance(self, point, origin):
        return abs(point.x - origin.x) ** 2 + abs(point.y - origin.y) ** 2