class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end -  start) // 2
            
            if A[mid] < target:
                start = mid
            else:
                end = mid  


        ret = []
        while len(ret) != k:
            if start is not None and start < 0:
                start = None

            if end is not None and end > len(A) - 1:
                end = None

            if start is None and end is None:
                break
            elif start is None:
                ret.append(A[end])
                end += 1
            elif end is None:
                ret.append(A[start])
                start -= 1
            else:
                if abs(A[start] - target) <= abs(A[end] - target):
                    ret.append(A[start])
                    start -= 1
                else:
                    ret.append(A[end])
                    end += 1
        return ret