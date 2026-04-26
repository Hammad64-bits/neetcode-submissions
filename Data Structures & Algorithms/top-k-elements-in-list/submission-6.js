class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let n = nums.length
        let map = {}

        for (let i = 0; i < n; i++){
            map[nums[i]] = (map[nums[i]] || 0) + 1
        }

        let bucket = Array.from({length: n + 1})
        for (const [key, value] of Object.entries(map)){
            if(!bucket[value]){
            bucket[value] = []
                
            }
            bucket[value].push([Number(key)])
        }

        let values = []
        for(let i = n ; i >= 0 && values.length < k; i--){
            if(bucket[i]){
                values.push(...bucket[i])
            }
        }

        return values
    }
}
