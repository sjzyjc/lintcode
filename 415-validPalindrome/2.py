class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        if s is None or len(s) == 0:
            return True

        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start +=1
                continue

            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1    

        return True

sl = Solution()
print(sl.isPalindrome(None))
print(sl.isPalindrome('ab'))
print(sl.isPalindrome('1a2'))

print(sl.isPalindrome('A man, a plan, a canal: Panama'))
print(sl.isPalindrome('race a car'))
                    