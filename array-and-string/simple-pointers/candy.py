'''
There are N children standing in a line. Each child is assigned a rating
value.

You are giving candies to these children subjected to the following
requirements:

Each child must have at least one candy. Children with a higher rating get
more candies than their neighbors. What is the minimum candies you must give?

Example 1:
Input: [1,0,2]
Output: 5
Explanation:
You can allocate to the first, second and third child with 2, 1, 2 candies
respectively.

Example 2:
Input: [1,2,2]
Output: 4
Explanation:
You can allocate to the first, second and third child with 1, 2, 1 candies
respectively. The third child gets 1 candy because it satisfies the above two
conditions.
'''


class Solution:
    def candy(self, ratings: list) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]
        updating = True
        while updating:
            updating = False
            for i in range(n):
                if i != 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    updating = True
                if i != n - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
                    updating = True

        sum = 0
        for candy in candies:
            sum += candy
        print(candies)
        return sum

    def candy_v2(self, ratings: list) -> int:
        n = len(ratings)
        left2right = [1 for _ in range(n)]
        right2left = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1

        sum = 0
        for i in range(n):
            sum += max(left2right[i], right2left[i])
        print(left2right, right2left)
        return sum

    def candy_v3(self, ratings: list) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        sum = 0
        for candy in candies:
            sum += candy
        print(candies)
        return sum

    def candy_v4(self, ratings: list) -> int:
        n = len(ratings)
        if n <= 1:
            return n

        def count(n):
            return n * (n + 1) // 2

        candies = 0
        pre_slope = up = down = 0
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            elif ratings[i] < ratings[i - 1]:
                new_slope = -1
            else:
                new_slope = 0
            if pre_slope < 0 and new_slope >= 0 or pre_slope > 0 and \
                    new_slope == 0:
                candies += count(up) + count(down) + max(up, down)
                up = 0
                down = 0
            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            else:
                candies += 1
            pre_slope = new_slope

        candies += count(up) + count(down) + max(up, down) + 1

        return candies


def test():
    s = Solution()
    array = [1, 0, 2, 1, 24, 24, 24, 3, 4, 11, 23, 1, 2]
    candiesSum = s.candy_v4(array)
    print(candiesSum)


if __name__ == '__main__':
    test()
