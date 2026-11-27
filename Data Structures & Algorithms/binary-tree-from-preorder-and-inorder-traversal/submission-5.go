/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func newNode(val int) *TreeNode {
	return &TreeNode{
		Val:val,
		Left:nil,
		Right:nil,
	}
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	inorder_map := make(map[int]int)
	for i,n := range inorder {
		inorder_map[n] = i
	}

	index := 0

	var dfs func(int, int) *TreeNode
	dfs = func(low,high int) *TreeNode {
		if low > high {
			return nil
		}

		root := newNode(preorder[index])
		index++

		root.Left = dfs(low, inorder_map[root.Val]-1)
		root.Right = dfs(inorder_map[root.Val]+1,high)

		return root
	}

	return dfs(0,len(preorder)-1)
}
