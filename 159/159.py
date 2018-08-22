class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end =  0, len(nums) -1
        last_index = end
        while start < end:
            mid = start + (end - start) // 2   
            
            if nums[mid] < nums[last_index]:
                end = mid
            else: 
                start = mid + 1    

        return nums[start]

