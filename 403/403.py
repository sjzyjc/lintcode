class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        if not A:
            return []
            
        ans_max_i, ans_max_j, ans_max = self.findMax(A, 1)
        ans_min_i, ans_min_j, ans_min = self.findMax(A, -1)
        
        if ans_max >= sum(A) + ans_min or ans_min_j - ans_min_i == len(A) - 1:
            return ans_max_i, ans_max_j
            
        return ans_min_j + 1, ans_min_i - 1
    
    def findMax(self, A, coef):
        i = j = cur_sum = 0
        prev_min = 0
        prev_index = -1
        max_sum = -(1 << 31)
        ans_i = ans_j = -1
        
        for index, val in enumerate(A):
            cur_sum += coef * val
            if cur_sum - prev_min > max_sum:
                max_sum = cur_sum - prev_min
                ans_i = prev_index
                ans_j = index
            
            if cur_sum < prev_min:
                prev_min = min(prev_min, cur_sum)
                prev_index = index
                
        return ans_i + 1, ans_j, max_sum

        
        