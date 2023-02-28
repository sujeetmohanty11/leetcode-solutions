class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)

        i = 0
        while nums[i] > target:
            i += 1

        return i


obj = Solution()
arr = [1, 3, 5, 6]
ser = 7

print(obj.searchInsert(arr, ser))
