class Solution:
    def encode(self, strs: List[str]) -> str:
        l = [ str(len(word)) for word in strs ]
        return ",".join(l) + ";" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        idx = s.find(";")
        if idx == 0: return []
        l = s[:idx].split(",")
        l = [ int(i) for i in l ]
        idx += 1
        res = []
        for n in l:
            res.append( s[idx:idx+n] )
            idx += n
        return res