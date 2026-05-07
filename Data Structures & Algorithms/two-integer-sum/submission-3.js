class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let lookup = {}
        for(let i = 0; i < nums.length; i++){
            let needed = target - nums[i]

            if(lookup[needed] != undefined){
                return [i, lookup[needed]]
            }

            lookup[nums[i]] = i
        }
    }
}
