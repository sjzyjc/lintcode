 class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        stack = []
        for num in A:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()
                
            if stack:
                stack[-1].right = node
                
            stack.append(node)

        return stack[0]