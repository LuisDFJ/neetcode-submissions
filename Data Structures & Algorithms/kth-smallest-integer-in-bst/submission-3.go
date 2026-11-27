/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
	var res int
	var inorder func(root *TreeNode)
	inorder = func(root*TreeNode) {
		if root == nil {
			return
		}

		inorder(root.Left)
		k--
		if k == 0 {
			res = root.Val
			return
		}
		inorder(root.Right)
	}
	inorder(root)
	return res
}
