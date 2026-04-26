class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        let map = {}
        let size = nums.length

        for(let i = 0; i < size; i++){
            map[nums[i]] = (map[nums[i]] || 0) + 1 
        }

        let bucket = Array.from({length: size + 1}, () => [])
        for (const [key, value] of Object.entries(map)){
            bucket[value].push(Number(key))
        }

        let res = []
        for(let j = size; j >= 0 && res.length < k; j--){
            if( bucket[j] !== [] ) res.push(...bucket[j])
        }

        return res
    }
}
