# LeetCode 169. Majority Element
#
# Problem Description:
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
#   Input:  nums = [3,2,3]
#   Output: 3
#
# Example 2:
#   Input:  nums = [2,2,1,1,1,2,2]
#   Output: 2
#
# Constraints:
#   n == nums.length
#   1 <= n <= 5 * 10^4
#   -10^9 <= nums[i] <= 10^9
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]



# ---- LeetCode Official Test Cases ----

import unittest


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # Example 1
        nums = [3, 2, 3]
        self.assertEqual(self.sol.majorityElement(nums), 3)

    def test_case_2(self):
        # Example 2
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(self.sol.majorityElement(nums), 2)

    def test_case_3(self):
        # Single element
        nums = [1]
        self.assertEqual(self.sol.majorityElement(nums), 1)

    def test_case_4(self):
        # All same elements
        nums = [6, 6, 6, 6]
        self.assertEqual(self.sol.majorityElement(nums), 6)

    def test_case_5(self):
        # Majority at the start, mixed values
        nums = [5, 5, 5, 5, 1, 2, 3]
        self.assertEqual(self.sol.majorityElement(nums), 5)

    def test_case_6(self):
        # Negative majority
        nums = [-1, -1, -1, 2, 3]
        self.assertEqual(self.sol.majorityElement(nums), -1)

    def test_case_7(self):
        # Even length, majority by one
        nums = [1, 1, 1, 1, 2, 2, 2, 3]
        self.assertEqual(self.sol.majorityElement(nums), 1)


if __name__ == "__main__":
    unittest.main()
