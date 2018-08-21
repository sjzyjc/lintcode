class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s):
        
        # write your code here
        if s is None or len(s) == 0:
            return ""

        start, end = 0, 0
        for i in range(len(s)):

            oddLength = self.expandAroundCenter(s, i, i)
            evenLength = self.expandAroundCenter(s, i, i+1)
            if oddLength > evenLength and oddLength > end - start + 1:
                end = i + (oddLength - 1)//2
                start = i - (oddLength - 1)//2

            if evenLength > oddLength and evenLength > end - start + 1:
                end = i + 1 + (evenLength - 2)//2
                start = i - (evenLength - 2)//2

        
        return s[start:end+1]


sl = Solution()
print(sl.longestPalindrome('adcde'))
