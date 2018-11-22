class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        # Write your code here
        if not nums:
            return 0
            
        f = [[(1 << 31) - 1 for _ in range(2)] for _ in range(len(nums) + 1)]
        
        f[0][0] = f[0][1] = 0
        
        for i in range(1, len(nums) + 1):
            for j in range(2):
                flip = 1 if nums[i - 1] != j else 0
                
                for prev in range(2):
                    if prev == 0 and j == 1:
                        continue
                    
                    f[i][j] = min(f[i][j], f[i - 1][prev] + flip)
                    
        return min(f[-1][0], f[-1][1])