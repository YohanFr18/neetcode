class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let values_set = new Set(nums)
        return nums.length === values_set.size ? false : true

    }
}
