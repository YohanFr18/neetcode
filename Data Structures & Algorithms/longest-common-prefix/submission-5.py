class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixo = []
        strs.sort()
        
        if strs[0] == '':
            return ""
                
        count = min(len(strs[0]), len(strs[-1]))
            
        for j in range(count):
            if strs[0][j] == strs[-1][j]:
                prefixo.append(strs[0][j])
            else:
                break
        return "".join(prefixo)