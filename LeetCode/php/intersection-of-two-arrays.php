class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function intersection($nums1, $nums2) {
        $ans = array();
        foreach($nums1 as $num) {
            if (in_array($num, $nums2) && !in_array($num, $ans)) {
                $ans[] = $num;
            }
        }
        return $ans;
    }
}


