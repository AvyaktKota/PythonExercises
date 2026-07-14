# LeetCode 1. Two Sum
#
# Problem Description:
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#   Input:  nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#   Input:  nums = [3,2,4], target = 6
#   Output: [1,2]
#
# Example 3:
#   Input:  nums = [3,3], target = 6
#   Output: [0,1]
#
# Constraints:
#   2 <= nums.length <= 10^4
#   -10^9 <= nums[i] <= 10^9
#   -10^9 <= target <= 10^9
#   Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# ---- LeetCode Official Test Cases ----

import unittest


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # Example 1
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_2(self):
        # Example 2
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_3(self):
        # Example 3: duplicate values, must be different indices
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_4(self):
        # Negative numbers
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_5(self):
        # Mixed positive and negative
        nums = [-3, 4, 3, 90]
        target = 0
        expected = [0, 2]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
