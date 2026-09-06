class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}
        for i in range(len(words)-1):
            minlen = min(len(words[i]),len(words[i+1]))
            if len(words[i]) > len(words[i+1]) and words[i][:minlen] == words[i+1][:minlen]:
                return ""
            for j in range(minlen):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break
        
        res = []
        visit = set()
        for char in adj:
            if not dfs(char,adj,visit,set(),res): return ""
        res.reverse()
        return "".join(res)

def dfs(char:str,adj:dict,visit:set,stack:set,res:list) -> bool:
    if char in stack: return False
    if char in visit: return True
    visit.add(char)
    stack.add(char)
    for neighbor in adj[char]:
        if not dfs(neighbor,adj,visit,stack,res): return False
    res.append(char)
    stack.remove(char)
    return True

        