class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_idx = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_idx:
                return [min(hash_idx[diff], i), max(hash_idx[diff], i)]
            hash_idx[n] = i
