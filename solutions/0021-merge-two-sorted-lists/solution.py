# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Dummy head node
        current = dummy     # Pointer for building the new list

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the rest of whichever list is not empty
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next  # Skip dummy and return head of new list
