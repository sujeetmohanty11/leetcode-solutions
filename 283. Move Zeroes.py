def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nums = sorted(nums)
    for i in nums:
        if i == 0:
            nums.remove(0)
        else:
            nums.append(0)
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
