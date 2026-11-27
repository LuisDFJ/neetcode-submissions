/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
    
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	arr := preorder_serialize(root)
	fmt.Println(arr)
	return strings.Join(arr,",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	return preorder_deserialize(strings.Split(data,","))
}

func preorder_deserialize(arr []string) *TreeNode {
	index := 0

	var dfs func() *TreeNode
	dfs = func() *TreeNode {
		if index ==  len(arr) {
			return nil
		}

		val := arr[index]
		index++

		if val == "N" { return nil }
		n,_ := strconv.Atoi(val)

		node := &TreeNode{
			Val:n,
			Left:nil,
			Right:nil,
		}
		node.Left = dfs()
		node.Right = dfs()
		return node
	}
	return dfs()
}

func preorder_serialize(root *TreeNode) []string {
	res := []string{}
	var dfs func(*TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			res = append(res, "N")
			return
		}
		res = append(res, strconv.Itoa(root.Val))
		dfs(root.Left)
		dfs(root.Right)
	}
	dfs(root)
	return res
}