# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append( self.merge(l1,l2) )
            lists = mergedLists
        return lists[0]
    
    def merge(self, l1: List[ListNode], l2: List[Optional[ListNode]]) -> ListNode:
        if not l2: return l1
        head = ListNode()
        tail = head
        while l1 and l2:
            l = None
            if l1.val < l2.val:
                l = l1
                l1 = l1.next
            else:
                l = l2
                l2 = l2.next
            tail.next = l
            tail = tail.next
        while l1:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        while l2:
            tail.next = l2
            tail = tail.next
            l2 = l2.next

        return head.next
        
