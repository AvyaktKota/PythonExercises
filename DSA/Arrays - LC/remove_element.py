# LeetCode 27. Remove Element
#
# Problem Description:
# Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The order of the elements may be changed. Then return the
# number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k. To
# get accepted, you need to do the following things:
#
#   1. Change the array nums such that the first k elements of nums contain the
#      elements which are not equal to val. The remaining elements of nums are
#      not important as well as the size of nums.
#   2. Return k.
#
# Custom Judge:
#   The judge will test your solution by calling the helper function:
#       int[] nums = [...]; // Input array
#       int val = ...;      // Value to remove
#       int[] expectedNums = [...]; // The expected answer with correct length.
#                                   // It is sorted with no values equaling val.
#       int k = removeElement(nums, val); // Calls your implementation
#       assert k == expectedNums.length;
#       sort(nums, 0, k); // Sort the first k elements of nums
#       for (int i = 0; i < expectedLength; i++) {
#           assert nums[i] == expectedNums[i];
#       }
#
# If all assertions pass, then your solution will be accepted.
#
# Example 1:
#   Input:  nums = [3,2,2,3], val = 3
#   Output: 2, nums = [2,2,_,_]
#   Explanation: Your function should return k = 2, with the first two elements
#   of nums being 2. It does not matter what you leave beyond the returned k
#   (hence they are underscores).
#
# Example 2:
#   Input:  nums = [0,1,2,2,3,0,4,2], val = 2
#   Output: 5, nums = [0,1,4,0,3,_,_,_]
#   Explanation: Your function should return k = 5, with the first five elements
#   of nums containing 0, 0, 1, 3, and 4. Note that the five elements can be
#   returned in any order. It does not matter what you leave beyond the returned
#   k (hence they are underscores).
#
# Constraints:
#   0 <= nums.length <= 100
#   0 <= nums[i] <= 50
#   0 <= val <= 100


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


# ---- LeetCode Official Test Cases ----

import unittest


class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _check(self, nums, val, expectedNums):
        # Mirrors the LeetCode custom judge.
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        kept = nums[:k]
        kept.sort()
        self.assertEqual(kept, expectedNums)
        return k

    def test_case_1(self):
        # Example 1
        nums = [3, 2, 2, 3]
        val = 3
        expectedNums = [2, 2]
        self._check(nums, val, expectedNums)

    def test_case_2(self):
        # Example 2
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expectedNums = [0, 0, 1, 3, 4]
        self._check(nums, val, expectedNums)

    def test_case_3(self):
        # Empty array
        nums = []
        val = 1
        expectedNums = []
        self._check(nums, val, expectedNums)

    def test_case_4(self):
        # All elements equal to val
        nums = [4, 4, 4, 4]
        val = 4
        expectedNums = []
        self._check(nums, val, expectedNums)

    def test_case_5(self):
        # No elements equal to val
        nums = [1, 2, 3, 4, 5]
        val = 6
        expectedNums = [1, 2, 3, 4, 5]
        self._check(nums, val, expectedNums)

    def test_case_6(self):
        # val at the boundaries
        nums = [2, 1, 0, 5, 2]
        val = 2
        expectedNums = [0, 1, 5]
        self._check(nums, val, expectedNums)

    def test_case_7(self):
        # Single element not equal to val
        nums = [1]
        val = 2
        expectedNums = [1]
        self._check(nums, val, expectedNums)

    def test_case_8(self):
        # Single element equal to val
        nums = [1]
        val = 1
        expectedNums = []
        self._check(nums, val, expectedNums)


if __name__ == "__main__":
    unittest.main()
