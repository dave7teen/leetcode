'''
Given an array of n positive integers and a positive integer s, find the
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3] Output: 2

Explanation:
the subarray [4,3] has the minimal length under the problem constraint.

Follow up: If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log n).
'''

from typing import List
import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        minimum_size = sys.maxsize

        def sum_of_subarray(i, j):
            sum = 0
            for num in nums[i:j + 1]:
                sum += num
            return sum

        for i in range(n):
            for j in range(i, n):
                if sum_of_subarray(i, j) >= s:
                    minimum_size = min(minimum_size, j - i + 1)
        return 0 if minimum_size == sys.maxsize else minimum_size

    def minSubArrayLen_v2(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        minimum_size = sys.maxsize
        for i in range(n):
            for j in range(i, n):
                pass


def test():
    solution = Solution()
    array = [2, 3, 1, 2, 4, 3]
    s = 7
    result = solution.minSubArrayLen(s, array)
    print(result)


if __name__ == '__main__':
    test()
