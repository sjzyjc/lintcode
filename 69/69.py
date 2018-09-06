"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
            
        queue = deque([root])
        ret = []
        level = 0
        while queue:
            length = len(queue)
            
            for i in range(length):
                node = queue.popleft()
                
                if not node:
                    continue
                
                if len(ret) - 1 < level:
                    ret.append([])
                ret[level].append(node.val)
            
                queue.append(node.left)
                queue.append(node.right)
            
            level += 1
               
        return ret       
            
