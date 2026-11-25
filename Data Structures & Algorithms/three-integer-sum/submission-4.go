import (
	"slices"
)

func threeSum(nums []int) [][]int {
	slices.Sort(nums)
	n := len(nums)
	res := [][]int{}
	for i := range n {
		// Skip values starting with the same sequence
		if i > 0 && nums[i] == nums[i-1] { continue }
		target := -nums[i]

		// Find left and right such that
		// nums[l] + nums[r] == -nums[i]
		l,r := i+1, n-1
		for l < r {
			sum := nums[l] + nums[r]
			if sum == target {
				res = append(res, []int{nums[i],nums[l],nums[r]})
				l++
				r--
				// Skip all values starting with the same sequence
				// now in l
				for l < r && nums[l] == nums[l-1] { l++ }
			} else if sum > target {
				r--
			} else {
				l ++
			}
		}
	}
	return res
}
