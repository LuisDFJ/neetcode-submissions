func genSet(nums []int) map[int]struct{} {
	res := make(map[int]struct{})
	for _,n := range nums {
		res[n] = struct{}{}
	}
	return res
}

func isIn(num int, set map[int]struct{}) bool {
	_, exists := set[num]
	return exists
}

func longestConsecutive(nums []int) int {
	set := genSet(nums)
	maxCount := 0
	for _,n := range nums {
		if !isIn(n-1,set) {
			count := 1
			for isIn(n+count,set) {
				count += 1
			}
			maxCount = max(maxCount, count)
		}
	}
	return maxCount
}
