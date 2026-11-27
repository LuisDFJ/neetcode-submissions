/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func relu(x int) int {
	return max(x,0)
}

func maxPathSum(root *TreeNode) int {
	var res int = root.Val
	var dfs func (*TreeNode) int
	dfs = func (root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := relu(dfs(root.Left))
		right := relu(dfs(root.Right))
		
		res = max(res, root.Val + left + right)

		return root.Val + max(left,right)
	}

	dfs(root)
	return res
}
