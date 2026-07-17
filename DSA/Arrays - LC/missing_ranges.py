# LeetCode 163. Missing Ranges
#
# Problem Description:
# You are given an inclusive integer range [lower, upper] and a sorted unique
# integer array nums, where all elements are within the inclusive range.
#
# Return the shortest sorted list of ranges that covers every missing number
# exactly. That is, no element of nums is in any of the ranges, and every
# missing number is in one of the ranges.
#
# Each range [a,b] is listed as [a,b] where a and b are inclusive.
#
# Example 1:
#   Input:  nums = [0,1,3,50,75], lower = 0, upper = 99
#   Output: [[2,2],[4,49],[51,74],[76,99]]
#   Explanation: The missing ranges are: [2,2], [4,49], [51,74], [76,99].
#
# Example 2:
#   Input:  nums = [-1], lower = -1, upper = -1
#   Output: []
#   Explanation: No missing ranges; -1 is the only number in the range.
#
# Constraints:
#   -10^9 <= lower <= upper <= 10^9
#   0 <= nums.length <= 10^4
#   nums is sorted in ascending order and all values are unique.
#   All values of nums are within the inclusive range [lower, upper].


from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ret_list = []
        for i in nums:
            if i > lower:
                ret_list.append([lower, i - 1])
            lower = i + 1
        

        if lower <= upper:
            ret_list.append([lower, upper])
        return ret_list



# ---- LeetCode Official Test Cases ----

import unittest


class TestMissingRanges(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _check(self, nums, lower, upper, expected):
        result = self.sol.findMissingRanges(list(nums), lower, upper)
        self.assertEqual(result, expected)

    def test_case_1(self):
        # Example 1
        nums = [0, 1, 3, 50, 75]
        lower, upper = 0, 99
        expected = [[2, 2], [4, 49], [51, 74], [76, 99]]
        self._check(nums, lower, upper, expected)

    def test_case_2(self):
        # Example 2: single number covering the whole range
        nums = [-1]
        lower, upper = -1, -1
        expected = []
        self._check(nums, lower, upper, expected)

    def test_case_3(self):
        # Empty array: the whole range is missing
        nums = []
        lower, upper = 0, 99
        expected = [[0, 99]]
        self._check(nums, lower, upper, expected)

    def test_case_4(self):
        # Missing only before the first element
        nums = [5, 10]
        lower, upper = 0, 10
        expected = [[0, 4]]
        self._check(nums, lower, upper, expected)

    def test_case_5(self):
        # Missing only after the last element
        nums = [0, 5]
        lower, upper = 0, 10
        expected = [[6, 10]]
        self._check(nums, lower, upper, expected)

    def test_case_6(self):
        # No missing ranges: nums covers [lower, upper] exactly
        nums = [0, 1, 2]
        lower, upper = 0, 2
        expected = []
        self._check(nums, lower, upper, expected)

    def test_case_7(self):
        # Gaps between consecutive elements
        nums = [1, 3, 7]
        lower, upper = 1, 7
        expected = [[2, 2], [4, 6]]
        self._check(nums, lower, upper, expected)


if __name__ == "__main__":
    unittest.main()
