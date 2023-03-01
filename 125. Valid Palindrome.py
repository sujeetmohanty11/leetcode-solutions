import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().replace(" ", "")
        for ele in s:
            if ele in string.punctuation:
                s = s.replace(ele, "")

        return s == s[::-1]



obj = Solution()
txt = """A man, a plan, a canal: Panama"""
print(obj.isPalindrome(txt))
