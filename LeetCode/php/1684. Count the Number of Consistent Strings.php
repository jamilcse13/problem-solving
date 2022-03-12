class Solution {

    /**
     * @param String $allowed
     * @param String[] $words
     * @return Integer
     */
    function countConsistentStrings($allowed, $words) {
        $allow = str_split($allowed);
        $count = 0;
        foreach ($words as $word) {
            $sentences = str_split($word);
            foreach ($sentences as $sentence) {
                $test = true;
                if (! in_array($sentence, $allow)) {
                    $test = false;
                    break;
                }
            }
            if ($test == true) {
                $count++;
            }
        }
        return $count;
    }
}


Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
