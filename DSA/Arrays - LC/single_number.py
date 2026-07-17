# LeetCode 136. Single Number
#
# Problem Description:
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
# Example 1:
#   Input:  nums = [2,2,1]
#   Output: 1
#
# Example 2:
#   Input:  nums = [4,1,2,1,2]
#   Output: 4
#
# Example 3:
#   Input:  nums = [1]
#   Output: 1
#
# Constraints:
#   1 <= nums.length <= 3 * 10^4
#   -3 * 10^4 <= nums[i] <= 3 * 10^4
#   Each element in the array appears twice except for one element which
#   appears only once.


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(0, len(nums), 2):
            
            if i == len(nums) - 1 or (nums[i] != nums[i+1]):
                return nums[i]



# ---- LeetCode Official Test Cases ----

import unittest


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # Example 1
        nums = [2, 2, 1]
        self.assertEqual(self.sol.singleNumber(nums), 1)

    def test_case_2(self):
        # Example 2
        nums = [4, 1, 2, 1, 2]
        self.assertEqual(self.sol.singleNumber(nums), 4)

    def test_case_3(self):
        # Example 3: single element
        nums = [1]
        self.assertEqual(self.sol.singleNumber(nums), 1)

    def test_case_4(self):
        # Negative numbers, single negative
        nums = [-1, -2, -2]
        self.assertEqual(self.sol.singleNumber(nums), -1)

    def test_case_5(self):
        # Single number at the end
        nums = [1, 2, 2, 3, 3]
        self.assertEqual(self.sol.singleNumber(nums), 1)

    def test_case_6(self):
        # Larger set with negative values
        nums = [-300, -100, -100, 0, 0, 50, -300, 50, 77]
        self.assertEqual(self.sol.singleNumber(nums), 77)


if __name__ == "__main__":
    unittest.main()
