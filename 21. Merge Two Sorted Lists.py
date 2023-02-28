class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if le
                new_list.append(i)
                list1.pop(i)
                new_list.append(j)

        return new_list


obj = Solution()
arr1 = [1, 2, 4]
arr2 = [3, 7, 8]
print(obj.mergeTwoLists(arr1, arr1))
