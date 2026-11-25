type Set struct {
	content map[rune]struct{}
}

func newSet() Set {
	return Set {
		content: make(map[rune]struct{}),
	}
}

func (s *Set) add(v rune) {
	s.content[v] = struct{}{}
}

func (s *Set) remove(v rune) {
	delete(s.content, v)
}

func (s *Set) in(v rune) bool {
	_,exists := s.content[v]
	return exists
}

func lengthOfLongestSubstring(s string) int {
	if s == "" { return 0 }
	set := newSet()
	maxL := 1
	left := 0
	for right := range s {
		for set.in(rune(s[right])) {
			set.remove(rune(s[left]))
			left ++
		}
		set.add(rune(s[right]))
		maxL = max(maxL, right - left + 1)
	}
	return maxL
}
