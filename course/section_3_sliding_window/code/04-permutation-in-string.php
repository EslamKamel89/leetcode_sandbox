<?php 

class Solution {

    function checkInclusion($s1, $s2) {

        $n = strlen($s1);
        $m = strlen($s2);

        if ($n > $m) {
            return false;
        }

        $pattern = [];
        $window = [];

        for ($i = 0; $i < $n; $i++) {
            $pattern[$s1[$i]] = ($pattern[$s1[$i]] ?? 0) + 1;
        }

        for ($i = 0; $i < $n; $i++) {
            $window[$s2[$i]] = ($window[$s2[$i]] ?? 0) + 1;
        }

        if ($window == $pattern) {
            return true;
        }

        for ($i = $n; $i < $m; $i++) {

            $entering = $s2[$i];
            $leaving = $s2[$i - $n];

            $window[$entering] = ($window[$entering] ?? 0) + 1;
            $window[$leaving]--;

            if ($window[$leaving] <= 0) {
                unset($window[$leaving]);
            }

            if ($window == $pattern) {
                return true;
            }
        }

        return false;
    }
}