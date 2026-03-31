class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_ana = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            hash_ana[key].append(string)
        return list(hash_ana.values())
