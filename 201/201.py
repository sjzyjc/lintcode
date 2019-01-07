"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start > end:
            return
        
        cur = SegmentTreeNode(start, end)
        
        if start == end:
            return cur
            
        mid = (start + end) // 2
        cur.left = self.build(start, mid)
        cur.right = self.build(mid + 1, end)
        
        return cur