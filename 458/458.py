class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start +1 < end:
            mid  = start + (end - start) // 2

            if nums[mid] == target:
                start =  mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if nums[end] == target:
            return end

        if nums[start] == target:
            return start

        return -1                    
