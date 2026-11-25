func productExceptSelf(nums []int) []int {
	n := len(nums)
	prefix := make([]int, n)
	postfix := make([]int, n)
	prefix[0] = 1
	postfix[0] = 1
	for i := range (n-1) {
		prefix[i+1] = nums[i] * prefix[i]
		postfix[i+1] = nums[n-1-i] * postfix[i]
	}

	res := []int{}
	for i := range n {
		res = append(res, prefix[i] * postfix[n-1-i])
	}

	return res

}
