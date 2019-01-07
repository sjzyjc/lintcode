class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        return self.helper(0, len(A) - 1, A)
        
    def helper(self, start, end, A):
        if start > end:
            return None
            
        cur = SegmentTreeNode(start, end, A[start])
        if start == end:
            return cur
            
        mid = (start + end) // 2
        cur.left = self.helper(start, mid, A)
        cur.right = self.helper(mid + 1, end, A)
        cur.val = max(cur.left.max, cur.right.max)
        
        return cur

sl = Solution()
sl.build([1, 2, 3, 4])