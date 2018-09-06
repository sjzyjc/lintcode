class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition >= k
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums and len(nums) == 0:
            return 0

        left, right = 0, len(nums) - 1

        while left < right:
            while left < right and nums[left] < k:
                left += 1

            while left < right and nums[right] >= k:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left

sl = Solution()
print(sl.partitionArray([0,1,1,1], -1))