class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = int(str(x)[1:][::-1])*-1

        return x if -2**31 <= x < 2**31 else 0


obj = Solution()
print(obj.reverse(-120))