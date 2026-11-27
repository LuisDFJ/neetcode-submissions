func push(stack *[]int, val int) {
	*stack = append(*stack, val)
}

func pop(stack *[]int) int {
	old := *stack
	n := len(old)
	val := old[n-1]
	*stack = old[:n-1]
	return val
}

func copy_stack(stack []int) []int {
	temp := make([]int, len(stack))
	copy(temp, stack)
	return temp
}

func combinationSum(nums []int, target int) [][]int {
	res := [][]int{}
	var dfs func (int, []int, int)
	dfs = func (index int, stack []int, total int) {
		if total == target {
			res = append(res, copy_stack(stack))
			return
		}
		if index >= len(nums) || total > target {
			return
		}

		push(&stack, nums[index])
		dfs(index, stack, total+nums[index])
		pop(&stack)
		dfs(index+1, stack, total)
	}
	dfs(0,[]int{},0)
	return res
}
