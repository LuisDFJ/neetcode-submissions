/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(n *TreeNode, m *TreeNode) bool {
	if n == nil || m == nil {
		return n == m
	}
	return n.Val == m.Val && isSameTree(n.Left, m.Left) && isSameTree(n.Right, m.Right)
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil || subRoot == nil {
		return root == subRoot
	}

	if isSameTree(root,subRoot) {
		return true
	}

	return isSubtree(root.Left,subRoot) || isSubtree(root.Right,subRoot)
}
