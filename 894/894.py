class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        # Write your code here
        if not array or len(array) == 0:
            return
        
        self.sort(array, 0)
        
    def sort(self, array, offset):
        if offset >= len(array) - 1:
            return 
        
        maxium = - (1 << 31)
        max_index = -1
        
        for index in range(len(array) - offset):
            if array[index] > maxium:
                max_index = index
                maxium = array[index]
        
        FlipTool.flip(array, max_index)
        FlipTool.flip(array, len(array) - offset - 1)

        self.sort(array, offset + 1)