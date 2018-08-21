class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        sqrtNum = num ** (1/2)

        for i in range(2, sqrtNum) and num > 1:
            print(i)


sl = Solution()
print(sl.primeFactorization(4))
