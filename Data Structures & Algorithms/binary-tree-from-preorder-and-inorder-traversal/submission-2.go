/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 import "slices"

func buildTree(preorder []int, inorder []int) *TreeNode {
    idx := 0

    var dfs func(int,int) *TreeNode
    dfs = func(left,right int) *TreeNode {
        var node *TreeNode
        if left <= right {
            node = &TreeNode{Val:preorder[idx]}
            pivot := slices.Index(inorder,preorder[idx])
            idx += 1
            node.Left = dfs(left,pivot-1)
            node.Right = dfs(pivot+1,right)
        }
        return node
    }
    return dfs(0,len(preorder)-1)
}
