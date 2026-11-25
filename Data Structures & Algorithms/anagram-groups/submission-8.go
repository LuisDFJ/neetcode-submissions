import (
	"slices"
)

func hashWord(s string) string {
	k := []rune(s)
	slices.Sort(k)
	return string(k)
}

func groupAnagrams(strs []string) [][]string {
	anagram_map := make(map[string][]string)
	for _,s := range strs {
		k := hashWord(s)
		anagram_map[k] = append(anagram_map[k], s)
	}

	res := [][]string{}
	for _,v := range anagram_map {
		res = append(res, v)
	}
	return res
}
