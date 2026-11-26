/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func merge(a,b *ListNode) *ListNode {
	head := &ListNode{Val:0,Next:nil}
	tail := head
	for a != nil && b != nil {
		if a.Val < b.Val {
			tail.Next = a
			a = a.Next
		} else {
			tail.Next = b
			b = b.Next
		}
		tail = tail.Next
	}

	if a != nil {
		tail.Next = a
	} else {
		tail.Next = b
	}

	return head.Next
}

func divide(lists []*ListNode, l,r int) *ListNode {
	if l == r {
		return lists[l]
	}

	m := (l+r)/2

	left := divide(lists,l,m)
	right := divide(lists,m+1,r)

	return merge(left,right)
}

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 { return nil }
	return divide(lists,0,len(lists)-1)
}
