# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        cur = head
        p = ListNode(cur.val)
        while cur:
            cur = cur.next
            if cur:
                p = ListNode(cur.val,p)
        return p

        