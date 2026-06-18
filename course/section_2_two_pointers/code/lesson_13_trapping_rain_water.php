<?php


class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function trap($height) {
        $max_left = [];
        $curr_max_left = 0;
        foreach ($height as $h) {
            $curr_max_left = max($curr_max_left, $h);
            $max_left[] = $curr_max_left;
        }
        $curr_max_right = 0;
        $water = 0;
        for ($i = count($height) - 1; $i >= 0; $i--) {
            $h = $height[$i];
            $curr_max_right = max($curr_max_right, $h);
            $newWater = min($curr_max_right, $max_left[$i]) - $h;
            if ($newWater > 0) {
                $water = $water + $newWater;
            }
        }
        return $water;
    }
}
