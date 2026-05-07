class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */


    topKFrequent(nums, k) {
        let lookup = {}

        for(let i = 0; i < nums.length; i++){
            lookup[nums[i]] = (lookup[nums[i]] || 0) + 1
        }

        let bucket = Array.from({length: nums.length + 1}, () => [])

        for(const [key, value] of Object.entries(lookup)){
            bucket[value].push(Number(key))
        }

        let res = []

        for(let i = bucket.length - 1; i >= 0 && res.length < k; i--){
            res.push(...bucket[i])
        }
        
        return res
    }
}
