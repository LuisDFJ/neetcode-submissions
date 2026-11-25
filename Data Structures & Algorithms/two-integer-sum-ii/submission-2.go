func res(i,j int) []int {
	return []int{i+1, j+1}
}

func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	for left < right {
		sum := numbers[left] + numbers[right]
		if sum == target {
			return res(left,right)
		} else if sum > target {
			right --
		} else {
			left ++
		}
	}
	return []int{}
}
