class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $map = array();
        foreach ($nums as $key=>$num){
            $map[$num]=$key;
        }
        foreach($nums as $key => $value){
            $targetItem = $target-$value;
            if(isset($map[$targetItem]) && $key!=$map[$targetItem]){
                return array($key,$map[$targetItem]);
            }
        }
        return array(0,0);
    }
}

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
