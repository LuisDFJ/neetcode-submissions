/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(root *TreeNode, low,high int) *TreeNode {
	if root == nil {
		return nil
	}
	if high < root.Val {
		return dfs(root.Left,low,high)
	} else if low > root.Val {
		return dfs(root.Right,low,high)
	} else {
		return root
	}
}

func lowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {
	if p == nil || q == nil {
		return nil
	}
	a,b := p.Val,q.Val
	return dfs(root,min(a,b),max(a,b))
}
