# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,prev = head,None
        while cur:
            tmp = cur.next
            # Change Connection To Prev Instead
            cur.next = prev
            # Advance: Prev Is Now Current
            prev = cur
            #           Current Is Now Next
            cur = tmp
        return prev
        