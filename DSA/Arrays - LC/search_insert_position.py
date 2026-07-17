# LeetCode 35. Search Insert Position
#
# Problem Description:
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
#   Input:  nums = [1,3,5,6], target = 5
#   Output: 2
#
# Example 2:
#   Input:  nums = [1,3,5,6], target = 2
#   Output: 1
#
# Example 3:
#   Input:  nums = [1,3,5,6], target = 7
#   Output: 4
#
# Constraints:
#   1 <= nums.length <= 10^4
#   -10^4 <= nums[i] <= 10^4
#   nums contains distinct values sorted in ascending order.
#   -10^4 <= target <= 10^4


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        
        while begin <= end:
            mid = (begin + end) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
            
        return begin



# ---- LeetCode Official Test Cases ----

import unittest


class TestSearchInsertPosition(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # Example 1: target present
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(self.sol.searchInsert(nums, target), 2)

    def test_case_2(self):
        # Example 2: target missing, insert in middle
        nums = [1, 3, 5, 6]
        target = 2
        self.assertEqual(self.sol.searchInsert(nums, target), 1)

    def test_case_3(self):
        # Example 3: target greater than all elements
        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(self.sol.searchInsert(nums, target), 4)

    def test_case_4(self):
        # Target less than all elements
        nums = [1, 3, 5, 6]
        target = 0
        self.assertEqual(self.sol.searchInsert(nums, target), 0)

    def test_case_5(self):
        # Single element, target present
        nums = [1]
        target = 1
        self.assertEqual(self.sol.searchInsert(nums, target), 0)

    def test_case_6(self):
        # Single element, target greater
        nums = [1]
        target = 2
        self.assertEqual(self.sol.searchInsert(nums, target), 1)

    def test_case_7(self):
        # Target equals first element
        nums = [2, 3, 5, 6]
        target = 2
        self.assertEqual(self.sol.searchInsert(nums, target), 0)

    def test_case_8(self):
        # Target between last two elements
        nums = [1, 3, 5, 6]
        target = 4
        self.assertEqual(self.sol.searchInsert(nums, target), 2)


if __name__ == "__main__":
    unittest.main()
