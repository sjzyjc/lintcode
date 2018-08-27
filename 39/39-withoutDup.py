class Solution:
    """
    @param nums: An integer array
    @return: nothing
    T: N S: 1
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        last_index = end
        while start < end:
            mid = start + (end - start) // 2    
            if nums[mid] > nums[last_index]:
                start =  mid + 1
            else:
                end = mid
        
        if start > 0:
            self.reverse(nums, 0, start - 1)
            self.reverse(nums, start, last_index)
            self.reverse(nums, 0, last_index)

        return nums        
        
    def reverse(self, nums, start, end):
        if start == 0:
            nums[start:end+1] = nums[end::-1]
        else:    
            nums[start:end+1] = nums[end:start-1:-1]

sl = Solution()
print(sl.recoverRotatedSortedArray([4,5,1,2,3]))        
