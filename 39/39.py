class Solution:
    """
    @param nums: An integer array
    @return: nothing
    T: N S: 1
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                self.reverse2(nums, 0, i)
                self.reverse2(nums, i+1, len(nums)-1)
                self.reverse2(nums, 0, len(nums)-1)

        return nums        
        
    def reverse(self, nums, start, end):
        if start == 0:
            nums[start:end+1] = nums[end::-1]
        else:    
            nums[start:end+1] = nums[end:start-1:-1]

    def reverse2(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

sl = Solution()
print(sl.recoverRotatedSortedArray([4,5,1,2,3]))        
