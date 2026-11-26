/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func length(head *ListNode) int {
	l := 0
	curr := head
	for curr != nil {
		l ++
		curr = curr.Next
	}
	return l
}

func split(head *ListNode, n int) (*ListNode, *ListNode) {
	var prev *ListNode
	curr := head
	for curr != nil && n > 0 {
		n --
		prev = curr
		curr = curr.Next
	}
	if prev != nil {
		prev.Next = nil
	}
	return head, curr
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

		a.Next, b.Next = b, aNext

		a,b = aNext,bNext
	}
}

func show(head *ListNode) {
	curr := head
	for curr != nil {
		fmt.Println(curr.Val)
		curr = curr.Next
	}
}

func reorderList(head *ListNode) {
	n := (length(head) + 1) / 2
	list_1, list_2 := split(head, n)
	list_2 = reverse(list_2)
	merge(list_1, list_2)
}