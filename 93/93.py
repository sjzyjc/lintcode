"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced, level = self.helper(root)
        return is_balanced
        
    def helper(self, root):
        if not root:
            return True, 0
            
        left_balanced, left_level = self.helper(root.left)
        right_balanced, right_level = self.helper(root.right)
        
        if not left_balanced or not right_balanced:
            return False, None
        
        if abs(left_level - right_level) > 1:
            return False, None
            
        return True, max(left_level, right_level) + 1

a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
a.left = b
a.right = c
sl = Solution()
print(sl.isBalanced(a))