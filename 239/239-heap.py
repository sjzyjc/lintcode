import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        
        heap = []
        ans = []
        for index in range(len(nums)):
            num = nums[index]                
            heapq.heappush(heap, -num)
            if index >= k:
                heap.remove(-nums[index - k])
                heapq.heapify(heap)
                
            if index >= k - 1:
                ans.append(-heap[0])
            
        return ans
            