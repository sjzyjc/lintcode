class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        sqrtNum = num ** (1/2)
        
        result = set()
        for k in range(2, int(sqrtNum) + 1):
            if num <= 1:
                break

            while num % k == 0:
                num = num / k 
                result.add(k)
        
        if num > 1:
            result.add(num)

        return result

sl = Solution()
print(sl.primeFactorization(4))
