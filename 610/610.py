class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return [-1, -1]
            
        nums.sort()
        if target < 0:
            target = -target
        
        right = 1
        for left in range(len(nums)):            
            while right < len(nums) and nums[right] - nums[left] < target:
                right += 1
                
            if left == right:
                right += 1
                
            if nums[right] - nums[left] == target:
                return [left +1, right + 1]

        return [-1,-1]