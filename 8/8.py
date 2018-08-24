class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, strr, offset):
        # write your code here
        str_list = list(strr)

        self.reverse2(str_list, 0, len(str_list) - 1 - offset)
        self.reverse2(str_list, len(str_list) - offset, len(str_list) - 1)
        self.reverse2(str_list, 0, len(str_list) - 1)

        return ''.join(str_list)

    def reverse(self, str_list, start, end):
        if start == 0:
            str_list[start:end+1] = str_list[end::-1]
        else:
            str_list[start:end+1] = str_list[end:start-1:-1]        

    def reverse2(self, nums, start, end):
        print(start,end)
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1        

sl = Solution()
print(sl.rotateString("abcdefg", 3))