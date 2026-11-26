/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if q == nil || p == nil {
		return q == p
	}
	return q.Val == p.Val && isSameTree(p.Right, q.Right) && isSameTree(p.Left, q.Left)
}
