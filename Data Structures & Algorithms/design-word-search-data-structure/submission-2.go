type Node struct {
	childs map[rune]*Node
	word bool
}

func newNode() *Node {
	return &Node {
		childs: make(map[rune]*Node),
		word: false,
	}
}

type WordDictionary struct {
	root *Node
}

func Constructor() WordDictionary {
	return WordDictionary {
		root: newNode(),
	}
}

func (this *WordDictionary) AddWord(word string)  {
	curr := this.root
	for _,r := range word {
		if _,exists := curr.childs[r]; !exists {
			curr.childs[r] = newNode()
		}
		curr = curr.childs[r]
	}
	curr.word = true
}

func (this *WordDictionary) Search(word string) bool {
	var dfs func(*Node, int) bool
	dfs = func(root *Node, i int) bool {
		if i == len(word) {
			return root.word
		}

		r := rune(word[i])

		if r == '.' {
			for _,child := range root.childs {
				if dfs(child,i+1) {
					return true
				}
			}
			return false
		}

		if _,exists := root.childs[r]; exists {
			return dfs(root.childs[r], i+1)
		}
		return false
	}

	return dfs(this.root, 0)
}
