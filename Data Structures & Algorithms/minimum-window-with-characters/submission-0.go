type Collector struct {
	letters map[rune]int
}

func newCollector() Collector {
	return Collector {
		letters: make(map[rune]int),
	}
}

func (c *Collector) add(v rune) {
	c.letters[v] += 1
}

func (c *Collector) remove(v rune) {
	c.letters[v] -= 1
}

func (c *Collector) isIn(v rune) bool {
	_,exists := c.letters[v]
	return exists
}

func (c *Collector) isRedundant(v rune, col *Collector) bool {
	return col.letters[v] > c.letters[v] || !c.isIn(v)
}

func (c *Collector) isValid( col *Collector ) bool {
	for k,v := range c.letters {
		if col.letters[k] < v {
			return false
		}
	}
	return true
}


func minWindow(s string, t string) string {
	t_col := newCollector()
	for _,r := range t {
		t_col.add(r)
	}

	w_col := newCollector()
	minS := ""
	minL := len(s)
	left := 0
	for right := range s {
		w_col.add(rune(s[right]))

		for left < right && t_col.isRedundant(rune(s[left]), &w_col) {
			w_col.remove(rune(s[left]))
			left ++
		}

		if t_col.isValid(&w_col) && minL >= (right-left+1) {
			minL = right-left + 1
			minS = s[left:right+1]
		}
	}
	return minS
}
