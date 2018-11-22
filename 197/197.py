import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        if not A:
            return 0
            
        total = math.factorial(len(A))
        
        offset = 0
        factorial = 1
        for i in range(len(A) - 2, -1, -1):
            count = 0
            for j in range(i + 1, len(A)):
                if A[j] > A[i]:
                    count += 1
                
            offset += count * factorial
            factorial *= (len(A) - i)
        
        return total - offset
                
            
