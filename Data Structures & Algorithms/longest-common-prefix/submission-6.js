class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let prefix = [];
        strs.sort();

        if (strs[0] === '') {
            return "";
        }

        const last_str = strs[strs.length - 1]
        const first_str = strs[0]

        let count = 0;
        if (first_str.length > last_str.length) {
            count = last_str.length;
        }
        else {
            count = first_str.length
        }

        for (let i = 0; i < count; i++) {
            if (first_str[i] === last_str[i]) {
                prefix.push(first_str[i]);
            }
            else {
                break
            }

        }
        return prefix.join("")
    }
}

