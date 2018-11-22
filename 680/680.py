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
        
        
        carry.append(s[start_index])
        self.permute(s, start_index + 1, carry, ans)
        carry.pop()
            
        if start_index < len(s) - 1:
            carry.append(s[start_index:start_index + 2])
            self.permute(s, start_index + 2, carry, ans)
            carry.pop()