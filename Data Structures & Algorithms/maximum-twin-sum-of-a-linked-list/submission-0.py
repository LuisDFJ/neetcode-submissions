# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        first,second = head,prev
        maxSum = 0
        while second:
            maxSum = max(first.val+second.val,maxSum)
            first = first.next
            second = second.next
        return maxSum
        