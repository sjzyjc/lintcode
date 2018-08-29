class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        self.mergeSort(A, 0, len(A) - 1)
        print(A)


    def mergeSort(self, A, start, end):
        if start >= end:
            return
        
        mid = (end + start) // 2
        self.mergeSort(A, start, mid)
        self.mergeSort(A, mid + 1, end)
        self.merge(A, start, end)

    def merge(self, A, start, end):
        tmp = []
        mid = (end + start) // 2
        first_half_index, second_half_index = start, mid + 1

        while first_half_index <= mid and second_half_index <= end:
            if A[first_half_index] <= A[second_half_index]:
                tmp.append(A[first_half_index])
                first_half_index += 1
            else:
                tmp.append(A[second_half_index])
                second_half_index += 1

        if first_half_index <= mid:
            tmp.extend(A[first_half_index : mid + 1])        

        if second_half_index <= end:
            tmp.extend(A[second_half_index : end + 1])
            
        for index, value in enumerate(tmp):
            A[start + index] = value

sl = Solution()
print(sl.sortIntegers2([3,2,1,4,5]))        