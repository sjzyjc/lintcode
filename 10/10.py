class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        if not str:
            return [""]
            
            
        ans = []
        str_list = list(str)
        str_list.sort()
        
        visited = [False for i in range(len(str_list))]
        self.permute(str_list, [], visited, ans)
        return ans
        
    def permute(self, str_list, carry, visited, ans):
        if len(carry) == len(str_list):
            ans.append("".join(carry))
            return
        
        for index in range(len(str_list)):
            if visited[index]:
                continue
            
            if index > 0 and str_list[index] == str_list[index - 1] and not visited[index - 1]:
                continue
            
            visited[index] = True
            carry.append(str_list[index])
            self.permute(str_list, carry, visited, ans)
            carry.pop()
            visited[index] = False
            
        
        