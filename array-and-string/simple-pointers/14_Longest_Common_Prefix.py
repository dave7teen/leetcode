"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.

Constraints:
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""


class Solution:
    # This approach has O(S) time complexity and O(S) space complexity. Since at worst scenario,
    # It compares all the strings with the newly created converted string array.
    def longestCommonPrefix(self, strs: list[str]) -> str:
        columns = [''.join(column) for column in tuple(zip(*strs))]
        result = ""
        if not columns:
            return result
        for column in columns:
            if not column == column[0] * len(strs):
                return result
            else:
                result += column[0]
        return result

    # Leetcode approach 1: horizontal scanning, with O(S) time complexity and O(1) space complexity.
    def longestCommonPrefix_v1(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

    # Approach 2: Vertical scanning
    def longestCommonPrefix_v2(self, strs: list[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) < i + 1 or strs[j][i] != letter:
                    return strs[0][:i]
        return strs[0]

    # Approach 3: Divide and conquer
    def __commonPrefix(self, left: str, right: str) -> str:
        min_length = min(len(left), len(right))
        for i in range(min_length):
            if left[i] != right[i]:
                return left[0:i]
        return left[0:min_length]

    def __LCP(self, strs: list[str], left_i: int, right_i: int) -> str:
        if left_i == right_i:
            return strs[left_i]
        mid = (left_i + right_i) // 2
        lcp_left = self.__LCP(strs, left_i, mid)
        lcp_right = self.__LCP(strs, mid + 1, right_i)
        return self.__commonPrefix(lcp_left, lcp_right)

    def longestCommonPrefix_v3(self, strs: list[str]) -> str:
        if not strs:
            return ""
        return self.__LCP(strs, 0, len(strs) - 1)

    # Approach 4:
    def __isCommonFix(self, strs: list[str], length: int) -> bool:
        str1 = strs[0][0:length]
        for i in range(1, len(strs)):
            if strs[i].find(str1) != 0:
                return False
        return True

    def longestCommonPrefix_v4(self, strs: list[str]) -> str:
        if not strs:
            return ""
        min_length = len(min(strs, key=len))
        left = 0
        right = min_length - 1
        while left <= right:
            mid = (left + right) // 2
            if self.__isCommonFix(strs, mid):
                left = mid + 1
            else:
                right = mid - 1
        return strs[0][:(left + right) // 2]


if __name__ == "__main__":
    # strs = ['ab', 'abc', 'abcd', 'abc']
    strs = ['flower', 'flow', 'flight']
    s = Solution()
    print("0. Output: ", s.longestCommonPrefix(strs))
    print("1. Output: ", s.longestCommonPrefix_v1(strs))
    print("2. Output: ", s.longestCommonPrefix_v2(strs))
    print("3. Output: ", s.longestCommonPrefix_v3(strs))
    print("4. Output: ", s.longestCommonPrefix_v4(strs))
