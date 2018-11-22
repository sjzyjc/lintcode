class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if not s:
            return None
            
        ans = []
        self.helper(s, 0, [0], ans)
        return ans
        
    def helper(self, s, start_index, carry, ans):
        if start_index == len(s):
            ans.append(self.getResult(s, carry))
            return
        
        for i in range(start_index, len(s)):
            substring = s[start_index: i + 1]
            if not self.isPalindrome(substring):
                continue
            
            carry.append(i + 1)
            self.helper(s, i + 1, carry, ans)
            carry.pop()
            
    def isPalindrome(self, string):
        start, end = 0, len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
                
        return True
        
    def getResult(self, s, carry):
        ans = []
        for index, value in enumerate(carry):
            if index > 0:
                ans.append(s[carry[index - 1] : carry[index]])
        
        return ans
    
sl = Solution()
print(sl.partition("abba"))