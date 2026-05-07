class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let lookup = {};

        for (let i = 0; i < strs.length; i++) {
            let sorted = strs[i].split("").sort().join("");
            if (lookup[sorted] != undefined) {
                lookup[sorted].push(strs[i]);
            } else {
                lookup[sorted] = [strs[i]];
            }
        }

        return Object.values(lookup)
    }
}
