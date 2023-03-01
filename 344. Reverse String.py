class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lst = []
        for i in range(0,len(s)):
            lst.insert(0, s[i])
        return lst


obj = Solution()
s = ["H","a","n","n","a","h"]
print(obj.reverseString(s))
