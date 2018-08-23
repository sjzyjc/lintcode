class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    T: logN S: 1
    """
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n

        ret = 1
        current_product = x
        while n != 0:
            if n % 2 == 1:
                ret = ret * current_product
            current_product = current_product * current_product    
            n = n // 2

        return ret    

sl = Solution()
print(sl.myPow(2,-3))        
print(sl.myPow(2,7))        