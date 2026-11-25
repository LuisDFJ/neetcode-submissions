func maxArea(heights []int) int {
	calcArea := func (l,r int) int {
		return (r-l) * min(heights[l],heights[r])
	}

	l,r := 0,len(heights)-1
	maxA := 0
	for l < r {
		maxA = max(calcArea(l,r),maxA)
		if heights[l] > heights[r] {
			r--
		} else {
			l++
		}
	}
	return maxA
}
