class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        let size = nums.length
        let myMap = {}

        for (let i = 0; i < size; i++){
            let needed = target - nums[i]
            if(myMap[needed] !== undefined) return [i, myMap[needed]]
            myMap[nums[i]] = i
        }
    }
}
