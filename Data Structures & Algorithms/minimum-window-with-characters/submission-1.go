type Counter struct {
	data map[rune]int
}

func newCounter() Counter {
	return Counter {
		data: make(map[rune]int),
	}
}

func (c *Counter) add(v rune) {
	c.data[v] += 1
}

func (c *Counter) remove(v rune) {
	c.data[v] -= 1
}

func (c *Counter) should_advance(v rune, ref *Counter) bool {
	return c.data[v] > ref.data[v]
}

func (c *Counter) is_valid(ref *Counter) bool {
	for k,v := range ref.data {
		if c.data[k] < v {
			return false
		}
	}
	return true
}

func minWindow(s string, t string) string {
	t_counter := newCounter()
	for _,c := range t {
		t_counter.add(c)
	}

	min_s := ""
	min_l := len(s)
	s_counter := newCounter()
	left := 0
	for right := range s {
		s_counter.add(rune(s[right]))
		for left < right && s_counter.should_advance(rune(s[left]), &t_counter) {
			s_counter.remove(rune(s[left]))
			left ++
		}

		if s_counter.is_valid(&t_counter) && right - left + 1 <= min_l {
			min_l = right - left + 1
			min_s = s[left:right+1]
		}
	}
	return min_s
}

	//{
		//X:1
		//Y:1
		//Z:1
	//}

	 //||
	//OUZODYXAZV
	//|||

	//{
		//O:0
		//U:0
		//Z:1
	//}
