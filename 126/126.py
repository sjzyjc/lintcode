"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        if not A:
            return None
        
        stack = []
        root = TreeNode(-(1 << 31))
        for index in range(len(A) + 1):
            num = A[index] if index != len(A) else (1 << 31) - 1
            node = None
            if index != len(A):
                node = TreeNode(num)
                
            while stack and stack[-1].val < num:
                cur = stack.pop()
                right_max = node
                left_max = stack[-1] if stack else None
                
                if left_max is None and right_max:
                    right_max.left = cur
                
                if right_max is None and left_max:
                    left_max.right = cur
                    
                if left_max and right_max:
                    if left_max.val < right_max.val:
                        left_max.right = cur
                    else:
                        right_max.left = cur
                    
                if cur.val > root.val:
                    root = cur
            
            stack.append(node)
            
        return root