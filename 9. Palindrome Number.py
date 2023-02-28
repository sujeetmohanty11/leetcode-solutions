class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)


obj = Solution()
x = -121
print(obj.isPalindrome(121))