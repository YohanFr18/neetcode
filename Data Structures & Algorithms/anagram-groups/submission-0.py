class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hashmap = {}
        
        for string in strs:
            key_curr = "".join(sorted(string))
            
            if key_curr not in hashmap:
                hashmap[key_curr] = [string]
            else:
                hashmap[key_curr].append(string)
        
        values_list = list(hashmap.values())
        
        return values_list