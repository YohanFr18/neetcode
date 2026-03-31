class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixo = ""
        strs.sort()
        if strs[0] == '':
            return ""

        if strs[0][0] != strs[-1][0]:
            return ""
            

        
        if len(strs[0]) < len(strs[-1]):
            count = len(strs[0])
        else:
            count = len(strs[-1])
            
        for j in range(count):
            if strs[0][j] == strs[-1][j]:
                prefixo += strs[0][j]
            else:
                break
        return prefixo