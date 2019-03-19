from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        
        queue = deque([])
        ans = []
        for index in range(len(nums)):
            num = nums[index]                
            while queue and queue[-1] < num:
                queue.pop()
                
            queue.append(num)
            if index >= k and nums[index - k] == queue[0]:
                queue.popleft()
                
            if index >= k - 1:
                ans.append(queue[0])
            
        return ans
            