class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, inputStr):
        # write your code here
        hashMap = {}
        for c in inputStr:
            if c in hashMap:
                del hashMap[c]
                continue
            hashMap[c] = True


        if len(hashMap) == 0:
            return len(inputStr)

        return len(inputStr) - len(hashMap) + 1       


sl = Solution()
print(sl.longestPalindrome('abccccdd'))
