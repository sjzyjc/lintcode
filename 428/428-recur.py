class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            n = -n
            x = 1/x  

        return self.fastPow(x, n)


    def fastPow(self, x, n):
        if n == 0:
            return 1

        half = self.fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x  


