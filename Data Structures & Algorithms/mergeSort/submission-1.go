// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func mergeSort(pairs []Pair) []Pair {
    merge := func (s,m,e int) {
        L := make([]Pair,m-s+1)
        R := make([]Pair,e-m)
        copy(L,pairs[s:m+1])
        copy(R,pairs[m+1:e+1])
        i,j,k := 0,0,s
        for i < len(L) && j < len(R) {
            if L[i].Key <= R[j].Key {
                pairs[k] = L[i]
                i += 1
            } else {
                pairs[k] = R[j]
                j += 1
            }
            k += 1
        }
        for i < len(L) {
            pairs[k] = L[i]
            i += 1
            k += 1
        }
        for j < len(R) {
            pairs[k] = R[j]
            j += 1
            k += 1
        }
    }
    var dfs func(int,int)
    dfs = func (s,e int) {
        if e - s > 0 {
            m := (e+s)/2
            dfs(s,m)
            dfs(m+1,e)
            merge(s,m,e)
        }
    }
    dfs(0,len(pairs)-1)
    return pairs
}
