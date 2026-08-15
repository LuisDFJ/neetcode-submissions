/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func abs(x int) int {
    if x < 0 { return -x }
    return x
}

func isBalanced(root *TreeNode) bool {
    if root == nil {return true}
    if isBalanced(root.Left) && isBalanced(root.Right) {
        return abs(height(root.Left) - height(root.Right)) < 2
    }
    return false
}

func height(root *TreeNode) int {
    if root == nil {return 0}
    return max(height(root.Left), height(root.Right)) + 1
}
