class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    T: logN S: 1
    """
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = 1 / x

        ret, current_product = 1, x
        while n > 0:
            if n&1 == 1:
                ret =  ret * current_product
            current_product = current_product * current_product

            n = n >> 1
        return ret    
            
sl = Solution()
print(sl.myPow(2,-3))        
print(sl.myPow(2,2))         