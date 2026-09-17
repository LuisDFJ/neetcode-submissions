class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            id = "".join(sorted(word))
            res[id].append(word)
        
        return [ v for v in res.values() ]
        