class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let word = ''
        for ( const str of strs){
            word += (String(str.length) + '#' + str)
        }
        return word
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i = 0
        let size = str.length
        let ans = []
        while(i < size){
            let j = i + 1
            while(str[j] !== '#') j++
            let length = Number(str.slice(i, j))
            ans.push(str.substr(j + 1, length ))
             i = j + length + 1
        }

        return ans
    }
}
