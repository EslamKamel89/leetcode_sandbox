<?php

class Solution {
    function mySqrt($x) {
        $left = 0;
        $right = $x;
        while ($left <= $right) {
            $m = intdiv($left + $right, 2);
            $sqr = $m *  $m;
            if ($sqr == $x) {
                return $m;
            }
            if ($sqr > $x) {
                $right = $m - 1;
            } else {
                $left = $m + 1;
            }
        }
        return $left - 1;
    }
}
