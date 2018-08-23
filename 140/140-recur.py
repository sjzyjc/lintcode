class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here

        if n < 0:
            n = -n 
            a = 1/a

        return self.calculatePow(a,b,n)

    def calculatePow(self, a, b, n):
        if n == 0:
            return 1 % b

        half_pow = self.calculatePow(a, b, n//2) % b
        if n % 2 == 1:
            ret = (half_pow * half_pow * a) % b 
        else:
            ret = (half_pow * half_pow) % b 
        return ret