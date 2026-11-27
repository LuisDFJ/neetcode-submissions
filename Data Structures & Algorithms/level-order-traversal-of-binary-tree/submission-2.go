/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Queue struct {
	data []*TreeNode
}

func newQueue() Queue {
	return Queue {
		data: []*TreeNode{},
	}
}

func (q *Queue) append(node *TreeNode) {
	if node != nil {
		q.data = append(q.data, node)
	}
}

func (q *Queue) pop() *TreeNode {
	l := len(q.data)
	if l == 0 { return nil }
	node := q.data[0]
	if l == 1 {
		q.data = []*TreeNode{}
	} else {
		q.data = q.data[1:]
	}
	return node
}

func (q *Queue) len() int {
	return len(q.data)
}

func levelOrder(root *TreeNode) [][]int {
	q := newQueue()
	q.append(root)

	res := [][]int{}

	for q.len() > 0 {
		level := []int{}
		for _ = range q.len() {
			node := q.pop()
			level = append(level, node.Val)
			for _,child := range []*TreeNode{node.Left, node.Right} {
				q.append(child)
			}
		}
		res = append(res, level)
	}
	return res
}
