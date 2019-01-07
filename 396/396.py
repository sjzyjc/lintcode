class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False
            
        f = [[0 for _ in range(len(values))] for _ in range(len(values))]
        
        for i in range(len(values)):
            f[i][i] = values[i]
            
        for l in range(2, len(values) + 1):
            for i in range(len(values) - l + 1):
                j = i + l - 1
                f[i][j] = max(values[i] - f[i + 1][j], values[j] - f[i][j - 1])
                
        return f[0][-1] > 0
                
            
                