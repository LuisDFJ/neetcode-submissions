type Collector struct {
	letters map[rune]int
	length int
}

func newCollector() Collector {
	return Collector {
		letters: make(map[rune]int),
		length: 0,
	}
}

func (c *Collector) add(r rune) {
	c.letters[r] += 1
	c.length += 1
}

func (c *Collector) remove(r rune) {
	c.letters[r] -= 1
	c.length -= 1
}

func (c *Collector) numReplacements() int {
	maxL := 0
	// May take up to O(26)
	// Since 26 <- [A-Z]
	for _,v := range c.letters {
		maxL = max(v,maxL)
	}
	// Having the letter with the highest freq.
	// this func returns the number of other letters.
	return c.length - maxL
}

func characterReplacement(s string, k int) int {
	collector := newCollector()
	left := 0
	maxL := 0
	for right := range s {
		collector.add(rune(s[right]))
		for collector.numReplacements() > k {
			collector.remove(rune(s[left]))
			left ++
		}
		maxL = max(maxL, right - left + 1)
	}
	return maxL
}
