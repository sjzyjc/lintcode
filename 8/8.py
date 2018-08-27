class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, strr, offset):
        if strr is None or len(strr) == 0:
            return ""
        # write your code here
        offset = offset % len(strr)
        self.reverse(strr, 0, len(strr) - 1 - offset)
        self.reverse(strr, len(strr) - offset, len(strr) - 1)
        self.reverse(strr, 0, len(strr) - 1)

    def reverse(self, strr, start, end):
        if start == 0:
            strr[start:end+1] = strr[end::-1]
        else:
            strr[start:end+1] = strr[end:start-1:-1]        