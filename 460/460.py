class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        left = self.findLastSmaller(A, target)
        print(left)
        right = left + 1

        ret = []
        while len(ret) != k:
            if self.isLeftSmallerOrEqual(A, left, right, target):
                ret.append(A[left])
                left -= 1
            else:
                ret.append(A[right])    
                right += 1

        return ret

    def findLastSmaller(self, A, target):
        start, end = 0, len(A) - 1

        while(start + 1 < end):
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else: 
                end = mid
        
        if A[end] < target:
            return end

        if A[start] < target:
            return start         

        return -1           

    def isLeftSmallerOrEqual(self, A, left, right, target):
        if left < 0:
            return False

        if right > len(A) - 1:
            return True

        if abs(A[left] - target) <= abs(A[right] - target):
            return True

        return False        

sl = Solution()
print(sl.kClosestNumbers([22,25,100,209,1000,1110,1111],15,5))