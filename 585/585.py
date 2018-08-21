class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here

        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end -  start) // 2
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid

        return nums[start]               