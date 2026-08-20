class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length){
            return false;
        }
        const ct = new Array(26).fill(0);
        for (let i = 0; i < s.length ; i++){
            ct[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            ct[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }
        return ct.every((val) => val === 0);
    }
}
