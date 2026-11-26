/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{Val:0, Next:nil}
	tail := head

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			tail.Next = list1
			tail = tail.Next
			list1 = list1.Next
		} else {
			tail.Next = list2
			tail = tail.Next
			list2 = list2.Next
		}
	}

	for list1 != nil {
		tail.Next = list1
		tail = tail.Next
		list1 = list1.Next
	}

	for list2 != nil {
		tail.Next = list2
		tail = tail.Next
		list2 = list2.Next
	}

	return head.Next
}
