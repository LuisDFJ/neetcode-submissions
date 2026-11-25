import (
	"cmp"
	"slices"
)

type KeyValue struct {
	K int
	V int
}

func topKFrequent(nums []int, k int) []int {
	counter := make(map[int]int)

	for _,n := range nums {
		counter[n] += 1
	}

	kv := []KeyValue{}
	for k,v := range counter {
		kv = append(kv, KeyValue{K:k, V:v})
	}

	slices.SortFunc(kv,
		func (a,b KeyValue) int {
			return cmp.Compare(b.V,a.V)
		},
	)

	res := []int{}
	for i := range k {
		res = append(res, kv[i].K)
	}

	return res
}
