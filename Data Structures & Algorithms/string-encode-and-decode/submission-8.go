
type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	sizes := []string{}
	for _, s := range strs {
		sizes = append(sizes, strconv.Itoa(len(s)))
	}
	res := fmt.Sprintf(
		"%s$%s",
		strings.Join(sizes, ";"),
		strings.Join(strs, ""),
	)
	return res
}

func (s *Solution) Decode(encoded string) []string {
	if encoded == "" {
		return []string{}
	}
	aux := strings.SplitN(encoded,"$",2)
	metadata := strings.Split(aux[0], ";")
	data := aux[1]
	res := []string{}
	for _,m := range metadata {
		l,_ := strconv.Atoi(m)
		res = append(res, data[:l])
		data = data[l:]
	}
	return res
}
