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
	return Queue{
		data: []*TreeNode{},
	}
}

func (q *Queue) push(n *TreeNode) {
	if n != nil {
		q.data = append(q.data,n)
	}
}

func (q *Queue) popleft() *TreeNode {
	l := len(q.data)
	if l == 0 {
		return nil
	}
	res := q.data[0]
	if l == 1 {
		q.data = []*TreeNode{}
	} else {
		q.data = q.data[1:]
	}
	return res
}

func (q *Queue) len() int {
	return len(q.data)
}

func levelOrder(root *TreeNode) [][]int {
	res := [][]int{}

	queue := newQueue()
	queue.push(root)
	for queue.len() > 0 {
		level := []int{}
		for _ = range queue.len() {
			node := queue.popleft()
			level = append(level,node.Val)
			for _,branch := range []*TreeNode{ node.Left, node.Right } {
				queue.push(branch)
			}
		} 
		res = append(res, level)
	}
	return res
}
