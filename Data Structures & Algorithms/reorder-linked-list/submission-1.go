/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func split(head *ListNode) (*ListNode, *ListNode) {
	fast, slow := head.Next, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	next := slow.Next
	slow.Next = nil
	return head, next
}

func reverse(head *ListNode) *ListNode {
	var prev *ListNode
	for head != nil {
		next := head.Next
		head.Next = prev
		prev = head
		head = next
	}
	return prev
}

func merge(a,b *ListNode) {
	for b != nil {
		aNext,bNext := a.Next, b.Next

		a.Next = b
		b.Next = aNext

		a,b = aNext, bNext
	}
}

func show(head *ListNode) {
	for head != nil {
		fmt.Println(head.Val)
		head = head.Next
	}
}

func reorderList(head *ListNode) {
	a,b := split(head)
	b = reverse(b)
	merge(a,b)
}
