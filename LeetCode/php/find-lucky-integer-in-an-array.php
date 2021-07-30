class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */    
    function findLucky($arr) {
    $unique_arr=array_count_values($arr);
    
    foreach($unique_arr as $key => $val)
    {
        if($key == $val)
        {
            $ans[] = $val;
        }
        
        }
        if (!$ans)
        {
            $ans[] = -1;
        }
        return max($ans);
    }
}
