# LeetCode 217. Contains Duplicate
#
# Problem Description:
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
# Example 1:
#   Input:  nums = [1,2,3,1]
#   Output: true
#
# Example 2:
#   Input:  nums = [1,2,3,4]
#   Output: false
#
# Example 3:
#   Input:  nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true
#
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)   
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
        


# ---- LeetCode Official Test Cases ----

import unittest


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # Example 1: contains duplicate
        nums = [1, 2, 3, 1]
        self.assertTrue(self.sol.containsDuplicate(nums))

    def test_case_2(self):
        # Example 2: all distinct
        nums = [1, 2, 3, 4]
        self.assertFalse(self.sol.containsDuplicate(nums))

    def test_case_3(self):
        # Example 3: contains duplicates
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(self.sol.containsDuplicate(nums))

    def test_case_4(self):
        # Single element
        nums = [1]
        self.assertFalse(self.sol.containsDuplicate(nums))

    def test_case_5(self):
        # Two identical elements
        nums = [2, 2]
        self.assertTrue(self.sol.containsDuplicate(nums))

    def test_case_6(self):
        # Negative numbers with duplicates
        nums = [-1, -2, -3, -1]
        self.assertTrue(self.sol.containsDuplicate(nums))

    def test_case_7(self):
        # Large range, all distinct
        nums = list(range(1000))
        self.assertFalse(self.sol.containsDuplicate(nums))


if __name__ == "__main__":
    unittest.main()
