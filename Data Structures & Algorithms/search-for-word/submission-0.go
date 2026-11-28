type Set map[[2]int]struct{}

func newSet() Set {
	return Set{}
}

func (s Set) add(d [2]int) {
	s[d] = struct{}{}
}

func (s Set) remove(d [2]int) {
	if s.isIn(d) {
		delete(s, d)
	}
}

func (s Set) isIn(d [2]int) bool {
	_,exists := s[d]
	return exists
}

func neighbors(n,m,N,M int, visited Set) [][2]int {
	res := [][2]int{}
	for _,d := range [][2]int{ {n-1,m}, {n+1,m}, {n,m-1}, {n,m+1} } {
		if d[0] >= 0 && d[0] < N && d[1] >= 0 && d[1] < M {
			if !visited.isIn(d) {
				res = append(res, d)
			}
		}
	}
	return res
}

func exist(board [][]byte, word string) bool {
	N,M := len(board), len(board[0])
	visited := newSet()

	var dfs func(int,int,int) bool
	dfs = func (i,j,k int) bool {
		if board[i][j] != word[k] {
			return false
		}
		if k == len(word) -1 {
			return true
		}

		visited.add([2]int{i,j})
		for _,neighbor := range neighbors(i,j,N,M,visited) {
			if dfs(neighbor[0],neighbor[1],k+1) {
				return true
			}
		}
		visited.remove([2]int{i,j})
		return false
	}

	for i := range N {
		for j := range M {
			if dfs(i,j,0) {
				return true
			}
		}
	}
	return false
}
