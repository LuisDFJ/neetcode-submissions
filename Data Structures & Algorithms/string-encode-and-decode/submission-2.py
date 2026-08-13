from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        lengths = [ str(len(s)) for s in strs ]
        return ",".join(lengths) + ";" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        i = s.find(";")
        if not i: return []
        lengths = [ int(l) for l in s[:i].split(",") ]
        arr = []
        start = end = i + 1
        for l in lengths:
            end += l
            arr.append( s[start:end] )
            start = end
        return arr

