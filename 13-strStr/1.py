class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        if len(target) == 0:
            return 0

        for i in range(len(source)):
            for j in range(len(target)):
                if i + j > len(source) - 1:
                    break
                    
                if source[i + j] != target[j]:
                    break

                if j == len(target) - 1 and source[i + j] == target[j]:
                    return i

        return -1


sl = Solution()

print(sl.strStr('aa', 'aaaaaaaaaa'))
