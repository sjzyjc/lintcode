class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        big = max(a, b)
        small = min(a, b)
        if small == 0:
            return big

        return self.gcd(small, big % small)

sl = Solution()
print(sl.gcd(10,15))