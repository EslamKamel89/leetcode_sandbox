<?php

class Solution {
    function findMaxAverage($nums, $k) {
        $currentSum = array_sum(array_slice($nums, 0, $k));
        $res = $currentSum;
        for ($i = $k; $i < count($nums); $i++) {
            $currentSum += $nums[$i];
            $currentSum -= $nums[$i - $k];
            $res = max($res, $currentSum);
        }
        return $res / $k;
    }
}
