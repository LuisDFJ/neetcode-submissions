# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        cur1 = list1
        cur2 = list2
        while cur1 or cur2:
            isC1Next = (cur1 and cur2) and (cur1.val < cur2.val) or not cur2
            if isC1Next:
                tail.next = cur1
                tail = tail.next
                cur1 = cur1.next
                tail.next = None
            else:
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next
                tail.next = None
        return head.next


