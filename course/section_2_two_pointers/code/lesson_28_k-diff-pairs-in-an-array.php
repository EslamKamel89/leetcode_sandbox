<?php


class Solution {

    function findPairs($nums, $k) {
        $count = 0;
        if ($k === 0) {
            $freq = [];
            foreach ($nums as $num) {
                $freq[$num] = ($freq[$num] ?? 0) + 1;
            }
            foreach ($freq as $_ => $f) {
                if ($f > 1) {
                    $count++;
                }
            }
            return $count;
        }
        $unique = array_flip($nums);
        foreach ($unique as $num => $_) {
            if (isset($unique[$num + $k])) {
                $count++;
            }
        }
        return $count;
    }
}
