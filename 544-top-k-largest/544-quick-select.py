class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    n + klogk
    1
    """
    def topk(self, nums, k):
        # write your code here
        if not nums or k <= 0:
            return []
            
        self.quickSelect(nums, len(nums) - k, 0, len(nums) - 1)
        
        ans = nums[len(nums) - k:]
        ans.sort(reverse = True)
        return ans
        
    def quickSelect(self, nums, k, start, end):
        if start >= end:
            return
        
        pivot =  nums[(start + end) // 2]
        left, right = start, end
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            
            while left <= right and nums[right] > pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if k >= left:
            self.quickSelect(nums, k, left, end)
        
        if k <= right:
            self.quickSelect(nums, k, start, right)