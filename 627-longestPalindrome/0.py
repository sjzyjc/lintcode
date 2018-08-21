class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, inputStr):
        # write your code here
        indexMap = {}
        for i in range(len(inputStr)):
            if inputStr[i] not in indexMap:
                indexMap[inputStr[i]] = 1
            else:
                indexMap[inputStr[i]] = indexMap[inputStr[i]] + 1
        print(indexMap)
        
        length = 0
        for j in indexMap:
            if indexMap[j] % 2 == 0:
                length += indexMap[j]
            else:
                if length % 2 == 0:
                    length += 1
                length += indexMap[j] - 1                

        return length    

sl = Solution()
print(sl.longestPalindrome('abccccdd'))
