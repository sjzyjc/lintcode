class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if b == 0:
            return -1
            
        if n < 0:
            n =  -n
            a = 1/a
            
        current_product = a
        ret = 1
        while n > 0:
            if n % 2 == 1:
                ret = ret * current_product % b
            current_product = current_product * current_product % b
            n = n // 2

        return ret % b   