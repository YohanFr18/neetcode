class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        aux_count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                aux_count+=1

        while aux_count > 0:
            nums.remove(val)
            aux_count -= 1
        
        k = len(nums)
        return k