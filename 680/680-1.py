class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if not s:
            return [[]]
        
        ans = []
        self.permute(s, 0, [], ans)
        return ans
        
    def permute(self, s, start_index, carry, ans):
        if start_index == len(s):
            ans.append(carry + [])
            return
        
        for i in range(1, 3):
            if start_index + i <= len(s):
                carry.append(s[start_index: start_index + i])
                self.permute(s, start_index + i, carry, ans)
                carry.pop()
