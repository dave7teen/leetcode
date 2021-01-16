'''
Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.

Image: https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
this case, 6 units of rain water (blue section) are being trapped. Thanks
Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6
'''

from typing import List


class Solution:
    # Brutal force
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(n):
            if i == 0 or i == n - 1:
                continue
            max_left = max_right = 0
            for j in range(i):
                max_left = max(max_left, height[j])
            for j in range(i + 1, n):
                max_right = max(max_right, height[j])
            if height[i] < max_left and height[i] < max_right:
                water += min(max_left, max_right) - height[i]
        return water

    # DP
    def trap_v2(self, height: List[int]) -> int:
        if not height:
            return 0
        water = 0
        n = len(height)
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        return water

    # Using Stacks solution
    def trap_v3(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        stack = []
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i],
                                     height[stack[-1]]) - height[top]
                water += distance * bounded_height
            stack.append(i)
        return water

    # Two pointer solution
    def trap_v4(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water



def test():
    s = Solution()
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    water = s.trap_v4(array)
    print(water)


if __name__ == '__main__':
    test()
