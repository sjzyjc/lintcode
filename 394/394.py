class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if not n or n == 0:
            return False
            
        if n == 1:
            return True
        
        remove_one = True
        remove_two = False
        
        for i in range(2, n + 1):
            win = (not remove_one) or (not remove_two)
            remove_two = remove_one
            remove_one = win
            
        return win
        