class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        for i in range(0,len(list1),2):
            for j in list2:
                list1.insert(i, j)
                list2.remove(j)
                print(j)
                continue
        return list1

obj = Solution()
arr1 = [1, 2, 4]
arr2 = [3, 7, 8]
print(obj.mergeTwoLists(arr1, arr1))
#output = [1,3,2,7,4,8]