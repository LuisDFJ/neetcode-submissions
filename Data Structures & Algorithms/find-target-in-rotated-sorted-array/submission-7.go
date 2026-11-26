// O(log n)
func find_pivot(nums []int) int {
	left, right := 0,len(nums)-1
	for left < right {
		mid := (left+right)/2
		if nums[mid] > nums[right] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

// O(log n)
func binary_search(nums []int, target int, offset int) int {
	left, right := 0,len(nums)-1
	for left <= right {
		mid := (left + right)/2
		if nums[mid] == target {
			return mid + offset
		} else if nums[mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}

// O(log n + log n) = O(log n)
func search(nums []int, target int) int {
	// O(log n)
	pivot := find_pivot(nums)
	right := len(nums)-1
	if target >= nums[pivot] && target <= nums[right] {
		// O(log n)
		return binary_search( nums[pivot:], target, pivot )
	} else {
		// O(log n)
		return binary_search( nums[:pivot], target, 0 )
	}
}