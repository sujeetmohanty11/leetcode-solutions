class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        temp = 0
        for i in arr:
            temp += min(i)
        return temp



obj = Solution()
arr = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(obj.minimumTotal(arr))