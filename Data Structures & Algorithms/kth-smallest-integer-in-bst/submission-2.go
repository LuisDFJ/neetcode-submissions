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
    var dfs func(*TreeNode)
    dfs = func(root *TreeNode) {
        if root == nil { return }
        dfs(root.Left)
        k -= 1
        if k == 0 {res = root.Val; return}
        dfs(root.Right)
    }
    dfs(root)
    return res
}
