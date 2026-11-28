type Node struct {
	childs map[rune]*Node
	word bool
}

func newNode() *Node {
	return &Node {
		childs: map[rune]*Node{},
		word: false,
	}
}

func (n *Node) isIn(c rune) bool {
	_,exists := n.childs[c]
	return exists
}

type PrefixTree struct {
	root *Node
}

func Constructor() PrefixTree {
	return PrefixTree {
		root: newNode(),
	}
}

func (this *PrefixTree) Insert(word string) {
	curr := this.root
	for _,r := range word {
		if !curr.isIn(r) {
			curr.childs[r] = newNode()
		}
		curr = curr.childs[r]
	}
	curr.word = true
}

func (this *PrefixTree) Search(word string) bool {
	curr := this.root
	for _,r := range word {
		if !curr.isIn(r) {
			return false
		}
		curr = curr.childs[r]
	}
	return curr.word
}

func (this *PrefixTree) StartsWith(prefix string) bool {
	curr := this.root
	for _,r := range prefix {
		if !curr.isIn(r) {
			return false
		}
		curr = curr.childs[r]
	}
	return true
}
