from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = [0 for _ in range(1 +  ord('z') - ord('a'))]
            for c in s:
                key[ord(c) - ord('a')] += 1
            d[tuple(key)].append(s)
        return [ l for _,l in d.items() ]

