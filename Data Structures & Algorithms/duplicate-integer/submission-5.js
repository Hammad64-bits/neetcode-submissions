class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {

        let dict = new Set()

        for(let num of nums){
            if(dict.has(num)){
                return true
            }
            dict.add(num)
        }
        return false
    }
}
