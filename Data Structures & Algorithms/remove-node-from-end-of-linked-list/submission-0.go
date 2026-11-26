/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func length(head *ListNode) int {
	l := 0
	for head != nil {
		l ++
		head = head.Next
	}
	return l
}

func removeNth(head *ListNode, n int) *ListNode {
	if n == 0 { return head.Next }
	curr := head
	for n - 1 > 0 {
		n --
		curr = curr.Next
	}
	curr.Next = curr.Next.Next
	return head
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	k := length(head) - n
	return removeNth(head, k)
}
