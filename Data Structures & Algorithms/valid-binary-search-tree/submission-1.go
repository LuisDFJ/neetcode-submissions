/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValid(root *TreeNode, low, high int) bool {
	if root == nil {
		return true
	}
	if root.Val > low && root.Val < high {
		return isValid(root.Left, low, root.Val) && isValid(root.Right, root.Val, high)

	}
	return false
}

func isValidBST(root *TreeNode) bool {
	return isValid(root, math.MinInt, math.MaxInt)
}
