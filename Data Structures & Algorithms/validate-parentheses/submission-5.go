type Stack struct {
	data []string
}

func newStack() Stack {
	return Stack {
		data: []string{},
	}
}
func (s *Stack) push(v string) {
	s.data = append(s.data, v)
}

func (s *Stack) pop() string {
	n := len(s.data)-1
	res := s.data[n]
	s.data = s.data[:n]
	return res
}

var couples = map[string]string{
	"(" : ")",
	"[" : "]",
	"{" : "}",
}

func isValid(s string) bool {
	stack := newStack()
	for _,c := range s {
		if _,exists := couples[string(c)]; exists {
			stack.push(string(c))
		} else if len(stack.data) > 0 {
			last_openning := couples[stack.pop()]
			if last_openning != string(c) {
				return false
			}
		} else {
			return false
		}
	}
	
	return len(stack.data) ==  0
}
