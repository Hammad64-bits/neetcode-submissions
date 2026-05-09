class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let lookup = {}

        for (let i = 0; i < nums.length; i++){
            lookup[nums[i]] = (lookup[nums[i]] || 0) + 1
        }

        console.log(lookup)

        let bucket = Array.from({length:nums.length + 1}, () => [])

        console.log(bucket)

        for (const [number, count] of Object.entries(lookup)){
            console.log(number, count)
            bucket[count] = [...bucket[count], Number(number)]
            console.log(bucket)
        }

        let res = []

        for (let i = bucket.length - 1; i >= 0 && res.length < k; i--){
            if(bucket[i].length === 0){
                continue
            }
            console.log(bucket[i])
            res.push(...bucket[i])
        }
            console.log(res)

        return res

    }
}
