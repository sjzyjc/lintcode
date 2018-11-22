class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        if target < 0 or not nums:
            return 0
            
        f = [0 for _ in range(target + 1)] 
        f[0] = 1
        prefix_sum = 0
        
        for i in range(1, len(nums) + 1):
            prefix_sum += nums[i - 1]
            for j in range(min(target, prefix_sum), nums[i - 1] - 1, -1):
                f[j] += f[j - nums[i - 1]]
            
        return f[-1]
