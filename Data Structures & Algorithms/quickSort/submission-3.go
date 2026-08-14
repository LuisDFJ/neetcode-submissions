// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

type Solution struct {

}

func NewSolution() *Solution {
    return &Solution{}
}

func QuickSort(pairs []Pair) []Pair {
    return dfs(pairs,0,len(pairs)-1)
}

func dfs(arr []Pair, s,e int) []Pair {
    if e-s > 0 {
        left := s
        for i := s ; i < e; i++ {
            if arr[i].Key < arr[e].Key {
                arr[left],arr[i] = arr[i],arr[left]
                left += 1
            }
        }
        arr[left],arr[e] = arr[e],arr[left]
        dfs(arr,s,left-1)
        dfs(arr,left+1,e)
    }
    return arr
}
