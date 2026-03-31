class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_ana = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            hash_ana[key].append(string)
        return list(hash_ana.values())