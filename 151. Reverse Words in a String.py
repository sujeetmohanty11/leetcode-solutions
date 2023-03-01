class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.strip().split()[::-1]
        txt = " "
        return txt.join(arr)


obj = Solution()
s = "the sky is blue"
# s = "  hello world  "
print(obj.reverseWords(s))
