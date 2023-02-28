# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return sorted(head)


obj = Solution()
arr = [-1, 5, 3, 4, 0]
print(obj.sortList(arr))
