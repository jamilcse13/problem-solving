class Solution {

    /**
     * @param String $sentence
     * @return Boolean
     */
    function checkIfPangram($sentence) {
        $alps = "abcdefghijklmnopqrstuvwxyz";
        foreach($alps as $alp_key => $alp) {
            foreach($sentence as $kay => $str) {
                if ($sentence[key] == $alp[alp_key]) {
                    $count++;
                    break;
                }
            }
        }
        if($count == 26)
            return true;
        else 
            return flase;
    }
}


Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Input: sentence = "leetcode"
Output: false
