class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0 or k==0:
            return []
        
        left, right = 0, k - 1
        
        ret = []
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        ret.append(window_sum)
        
        while right < len(nums) - 1:
            window_sum = window_sum - nums[left] + nums[right + 1]
            right += 1
            left += 1
            ret.append(window_sum)
            
        return ret    
