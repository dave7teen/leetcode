'''
Given an array nums of n integers where n > 1, return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Example:
Input: [1,2,3,4] Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up: Could you solve it with constant space complexity? (The output
array does not count as extra space for the purpose of space complexity
analysis.)
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> list:
        n = len(nums)
        result = [1 for _ in range(n)]
        product_forward = product_backward = 1
        for i in range(n):
            result[i] *= product_forward
            result[n - 1 - i] *= product_backward
            product_forward *= nums[i]
            product_backward *= nums[n - 1 - i]
        return result


def test():
    s = Solution()
    array = [1, 2, 3, 4]
    result = s.productExceptSelf(array)
    print(result)


if __name__ == '__main__':
    test()
