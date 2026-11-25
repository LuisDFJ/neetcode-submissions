func isAlphanum(c rune) bool {
	return unicode.IsLetter(c) || unicode.IsNumber(c)
}

func same(a,b rune) bool {
	return unicode.ToLower(a) == unicode.ToLower(b)
}

func isPalindrome(s string) bool {
	left, right := 0, len(s)-1
	for left < right {
		for left < right && !isAlphanum(rune(s[left])) {
			left++
		}
		for left < right && !isAlphanum(rune(s[right])) {
			right--
		}

		if !same(rune(s[right]), rune(s[left])) {
			return false
		}
		left ++
		right --
	}
	return true
}
