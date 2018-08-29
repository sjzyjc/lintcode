class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        index_map = {}


        for index,i in enumerate(nums):
            if i - target in index_map:
                return [min(index + 1, index_map[i - target]),max(index + 1, index_map[i - target])]

            if i + target in index_map:
                return [min(index + 1, index_map[i + target]),max(index + 1, index_map[i + target])]

            index_map[i] = index + 1

sl = Solution()
print(sl.twoSum7([2,7,15,24], 5))