class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here

        if source is None or target is None:
            return -1

        if len(target) == 0:
            return 0

        if len(target) > len(source):
            return -1

        power = 31 ** (len(target) - 1)
        targetHash, initSourceHash = 0, 0
        mod = 10**6

        for i in range(len(target)):
            targetHash = (targetHash * 31 + ord(target[i])) % mod
            initSourceHash = (initSourceHash * 31 + ord(source[i])) % mod

        if targetHash == initSourceHash:
            return 0

        for j in range(len(source)):
            if initSourceHash != targetHash:
                popup = initSourceHash - ((ord(source[j])*power) % mod)

                if popup < 0:
                    popup += mod
                
                if j + len(target) > len(source) - 1:
                    break
                initSourceHash = (
                    popup * 31 + ord(source[j + len(target)])) % mod

                if initSourceHash < 0:
                    initSourceHash += mod

                continue

            return j

        return -1


sl = Solution()
print(sl.strStr('abcde', 'e'))
