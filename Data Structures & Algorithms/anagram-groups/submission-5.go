func groupAnagrams(strs []string) [][]string {
	counts := make(map[[26]int][]string)
	
	for _, s := range strs {
		count := [26]int{}
		for _, c := range s {
			count[c - 'a']++
		}
		if counts[count] == nil {
			counts[count] = make([]string, 0)
		}
		counts[count] = append(counts[count], s)
	}
	
	res := make([][]string, 0, len(counts))
	for _, v := range counts {
		res = append(res, v)
	}
	
	return res
}

