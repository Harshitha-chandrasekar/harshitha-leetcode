# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def LastNode(h):
            while h.next.next:
                h = h.next
            Nnode = h.next
            h.next = None
            return Nnode

        temp = head
        while temp.next and temp.next.next:
            insert = LastNode(temp)
            insert.next = temp.next
            temp.next = insert
            temp = temp.next.next
