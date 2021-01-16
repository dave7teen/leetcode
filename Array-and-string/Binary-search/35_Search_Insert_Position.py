"""
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Example 4:
    Input: nums = [1,3,5,6], target = 0
    Output: 0

Example 5:
    Input: nums = [1], target = 0
    Output: 0

Constraints:
    1 <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
    nums contains distinct values sorted in ascending order.
    -10**4 <= target <= 10**4
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 6]
    s = Solution()
    print("Input: 2, Output: ", s.searchInsert(nums, 2))
    print("Input: 4, Output: ", s.searchInsert(nums, 4))
