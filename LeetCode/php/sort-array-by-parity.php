class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortArrayByParity($nums) {
        $even_num = [];
        $odd_num = [];
        foreach ($nums as $num) {
            $num%2 ? $odd_num[] = $num : $even_num[] = $num;
        }
        return array_merge($even_num, $odd_num);
    }
}


Input: nums = [3,1,2,4]
Output: [2,4,3,1]
