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
            
        f = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        f[0][0] = 1
        
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                f[i][j] = f[i - 1][j]
                if j >= nums[i - 1]:
                    f[i][j] += f[i - 1][j - nums[i - 1]]
                    
        return f[-1][-1]
