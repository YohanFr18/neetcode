class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_count = {}
        for number in nums:
            hash_count[number] = 1 + hash_count.get(number, 0)

        vals = sorted(list(hash_count.values()), reverse=True)
        answer = []

        for i in range(k):
            for key in list(hash_count.keys()):
                if hash_count[key] == vals[i]:
                    answer.append(key)
                    del hash_count[key]
                    break
        return answer