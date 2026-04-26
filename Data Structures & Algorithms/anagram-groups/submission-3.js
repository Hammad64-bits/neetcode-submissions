class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        let size = strs.length
        let myMap = {}

        for (let i = 0; i < size; i++){
            let word = strs[i].split("").sort().join("")
            if(myMap[word] === undefined) myMap[word] = [strs[i]]
            else myMap[word].push(strs[i]) 
        }
            

        return Object.values(myMap)
    }
}
